import operator
import uuid
from functools import reduce
from typing import Dict, Iterable, List, Set

import numpy as np
import pandas as pd
from sqlalchemy import (
    Column,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    delete,
    select,
    text,
)

from ..core.chunk_store import ChunkStore
from ..core.types import (
    Chunk,
    ChunkBatch,
    ChunkId,
    CustomIdSupervisedBatch,
    NewChunkBatch,
    SupervisedBatch,
)
from .constraints import Constraint


def get_sql_columns(df: pd.DataFrame):
    columns = []
    for col in df.columns:
        dtype = df[col].dtype
        if dtype == int:
            columns.append(Column(col, Integer))
        elif dtype == float:
            columns.append(Column(col, Float))
        elif dtype == object:
            columns.append(Column(col, String))
        else:
            raise ValueError(
                f"Column {col} has dtype {str(dtype)} which is not a supported type for metadata columns."
            )
    return columns


class SQLiteChunkStore(ChunkStore):
    def __init__(self, in_memory=True, **kwargs):
        super().__init__(**kwargs)

        if in_memory:
            self.engine = create_engine(f"sqlite:///:memory:")
        else:
            self.db_name = f"{uuid.uuid4()}.db"
            self.engine = create_engine(f"sqlite:///{self.db_name}")

        self.metadata = MetaData()

        self.chunk_table = Table(
            "neural_db_chunks",
            self.metadata,
            Column("chunk_id", Integer, primary_key=True),
            Column("custom_id", Integer),
            Column("text", String),
            Column("keywords", String),
            Column("document", String),
        )
        self.metadata.create_all(self.engine)

        self.custom_id_table = None

        self.metadata_table = None

        self.next_id = 0

    def _write_to_table(self, df: pd.DataFrame, table: Table):
        df.to_sql(
            table.name,
            con=self.engine,
            dtype={c.name: c.type for c in table.columns},
            if_exists="append",
            index=False,
        )

    def _create_custom_id_table(self, integer_custom_ids):
        custom_id_dtype = Integer if integer_custom_ids else String
        self.custom_id_table = Table(
            "neural_db_custom_ids",
            self.metadata,
            Column("custom_id", custom_id_dtype, primary_key=True),
            Column("chunk_id", Integer),
        )
        self.metadata.create_all(self.engine)

    def _store_custom_ids(self, custom_ids, chunk_ids):
        batch_integer_custom_ids = custom_ids.dtype == int
        if self.custom_id_table is None:
            self._create_custom_id_table(integer_custom_ids=batch_integer_custom_ids)

        table_integer_custom_ids = isinstance(
            self.custom_id_table.columns.custom_id.type, Integer
        )

        if table_integer_custom_ids != batch_integer_custom_ids:
            raise ValueError(
                "Custom ids must all have the same type. Found some custom ids with type int, and some with type str."
            )

        custom_id_df = pd.DataFrame({"custom_id": custom_ids, "chunk_id": chunk_ids})
        self._write_to_table(df=custom_id_df, table=self.custom_id_table)

    def _add_metadata_column(self, column: Column):
        column_name = column.compile(dialect=self.engine.dialect)
        column_type = column.type.compile(self.engine.dialect)
        stmt = text(
            f"ALTER TABLE {self.metadata_table.name} ADD COLUMN {column_name} {column_type}"
        )

        with self.engine.begin() as conn:
            conn.execute(stmt)

        # This is so that sqlalchemy recognizes the new column.
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)
        self.metadata_table = Table(
            self.metadata_table.name, self.metadata, autoload_with=self.engine
        )

    def _store_metadata(self, metadata: pd.DataFrame, chunk_ids: pd.Series):
        metadata_columns = get_sql_columns(metadata)
        if self.metadata_table is None:
            self.metadata_table = Table(
                "neural_db_metadata",
                self.metadata,
                Column("chunk_id", Integer, primary_key=True),
                *metadata_columns,
            )
            self.metadata.create_all(self.engine)
        else:
            for column in metadata_columns:
                if column.name not in self.metadata_table.columns:
                    self._add_metadata_column(column=column)
                else:
                    if str(column.type) != str(
                        self.metadata_table.columns[column.name].type
                    ):
                        raise ValueError(
                            f"Existing metadata for column {column.name} has type {str(self.metadata_table.columns[column.name].type)} but new metadata has type {str(column.type)}."
                        )
        metadata["chunk_id"] = chunk_ids
        self._write_to_table(df=metadata, table=self.metadata_table)

    def insert(self, chunks: Iterable[NewChunkBatch], **kwargs) -> Iterable[ChunkBatch]:
        inserted_batches = []
        for batch in chunks:
            chunk_ids = pd.Series(
                np.arange(self.next_id, self.next_id + len(batch), dtype=np.int64)
            )
            self.next_id += len(batch)

            chunk_df = batch.to_df()
            chunk_df["chunk_id"] = chunk_ids

            if batch.custom_id is not None:
                self._store_custom_ids(custom_ids=batch.custom_id, chunk_ids=chunk_ids)

            if batch.metadata is not None:
                self._store_metadata(batch.metadata, chunk_ids=chunk_ids)

            self._write_to_table(df=chunk_df, table=self.chunk_table)

            inserted_batches.append(
                ChunkBatch(
                    chunk_id=chunk_ids,
                    text=batch.text,
                    keywords=batch.keywords,
                )
            )

        return inserted_batches

    def delete(self, chunk_ids: List[ChunkId], **kwargs):
        delete_chunks = delete(self.chunk_table).where(
            self.chunk_table.c.chunk_id.in_(chunk_ids)
        )
        delete_metadata = delete(self.metadata_table).where(
            self.metadata_table.c.chunk_id.in_(chunk_ids)
        )
        with self.engine.begin() as conn:
            conn.execute(delete_chunks)
            conn.execute(delete_metadata)

    def get_chunks(self, chunk_ids: List[ChunkId], **kwargs) -> List[Chunk]:

        id_to_chunk = {}

        chunk_stmt = select(self.chunk_table).where(
            self.chunk_table.c.chunk_id.in_(chunk_ids)
        )
        metadata_stmt = select(self.metadata_table).where(
            self.metadata_table.c.chunk_id.in_(chunk_ids)
        )
        with self.engine.connect() as conn:
            for row in conn.execute(chunk_stmt).all():
                id_to_chunk[row.chunk_id] = Chunk(
                    custom_id=row.custom_id,
                    text=row.text,
                    keywords=row.keywords,
                    document=row.document,
                    chunk_id=row.chunk_id,
                    metadata=None,
                )
            for row in conn.execute(metadata_stmt).all():
                metadata = row._asdict()
                del metadata["chunk_id"]
                id_to_chunk[row.chunk_id].metadata = metadata

        chunks = []
        for chunk_id in chunk_ids:
            if chunk_id not in id_to_chunk:
                raise ValueError(f"Could not find chunk with id {chunk_id}.")
            chunks.append(id_to_chunk[chunk_id])

        return chunks

    def filter_chunk_ids(
        self, constraints: Dict[str, Constraint], **kwargs
    ) -> Set[ChunkId]:
        if not len(constraints):
            raise ValueError("Cannot call filter_chunk_ids with empty constraints.")

        condition = reduce(
            operator.and_,
            [
                constraint.sql_condition(column_name=column, table=self.metadata_table)
                for column, constraint in constraints.items()
            ],
        )

        stmt = select(self.metadata_table.c.chunk_id).where(condition)

        chunk_ids = set()
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                chunk_ids.add(row.chunk_id)

        return chunk_ids

    def remap_custom_ids(
        self, samples: Iterable[CustomIdSupervisedBatch]
    ) -> Iterable[SupervisedBatch]:
        remapped_batches = []

        for batch in samples:
            chunk_ids = []
            with self.engine.connect() as conn:
                for custom_ids in batch.custom_id:
                    sample_ids = []
                    for custom_id in custom_ids:
                        stmt = select(self.custom_id_table.c.chunk_id).where(
                            self.custom_id_table.c.custom_id == custom_id
                        )
                        if result := conn.execute(stmt).first():
                            sample_ids.append(result.chunk_id)
                        else:
                            raise ValueError(
                                f"Could not find chunk with custom id {custom_id}."
                            )
                    chunk_ids.append(sample_ids)

            remapped_batches.append(
                SupervisedBatch(query=batch.query, chunk_id=pd.Series(chunk_ids))
            )

        return remapped_batches
