# tests/integration_tests/test_vectorstores.py
from typing import AsyncGenerator, Generator

import pytest
from langchain_core.vectorstores import VectorStore
from langchain_tests.integration_tests.vectorstores import (
    AsyncReadWriteTestSuite,
    ReadWriteTestSuite,
)

from langchain_zeusdb.vectorstores import ZeusDBVectorStore


class TestZeusDBVectorStore(ReadWriteTestSuite):
    """Test sync operations of ZeusDBVectorStore."""

    @pytest.fixture()
    def vectorstore(self) -> Generator[VectorStore, None, None]:
        """Get an empty vectorstore for integration tests."""
        from zeusdb import VectorDatabase

        vdb = VectorDatabase()
        # Use EMBEDDING_SIZE=6 from langchain_tests
        index = vdb.create("hnsw", dim=6, space="cosine")
        store = ZeusDBVectorStore(zeusdb_index=index, embedding=self.get_embeddings())

        try:
            yield store
        finally:
            # Cleanup if needed - ZeusDB doesn't require special cleanup
            pass


class TestZeusDBVectorStoreAsync(AsyncReadWriteTestSuite):
    """Test async operations of ZeusDBVectorStore."""

    @pytest.fixture()
    async def vectorstore(self) -> AsyncGenerator[VectorStore, None]:
        """Get an empty vectorstore for async integration tests."""
        from zeusdb import VectorDatabase

        vdb = VectorDatabase()
        # Use EMBEDDING_SIZE=6 from langchain_tests
        index = vdb.create("hnsw", dim=6, space="cosine")
        store = ZeusDBVectorStore(zeusdb_index=index, embedding=self.get_embeddings())

        try:
            yield store
        finally:
            # Cleanup if needed - ZeusDB doesn't require special cleanup
            pass


@pytest.mark.compile
def test_integration_compile_check() -> None:
    """Compilation check for integration tests."""
    # This test just verifies that imports work

    from zeusdb import VectorDatabase  # noqa: F401

    from langchain_zeusdb import ZeusDBVectorStore  # noqa: F401

    # If we get here, imports compiled successfully
    assert True
