"""Unit tests for langchain-zeusdb imports and basic functionality."""


def test_imports() -> None:
    """Test that all public imports work correctly."""
    from langchain_zeusdb import AsyncZeusDBVectorStore, ZeusDBVectorStore
    from langchain_zeusdb.vectorstores import (
        get_langchain_requirements,
        is_langchain_available,
    )

    assert ZeusDBVectorStore is not None
    assert AsyncZeusDBVectorStore is not None
    assert is_langchain_available() is True
    assert "langchain-core" in get_langchain_requirements()[0]


def test_utility_functions() -> None:
    """Test utility functions without requiring ZeusDB index."""
    from langchain_zeusdb.vectorstores import ZeusDBVectorStore

    # Test static methods that don't need an index
    assert ZeusDBVectorStore._extract_index_dim(None) is None

    # Test vector distance calculation
    v1 = [1.0, 0.0, 0.0]
    v2 = [0.0, 1.0, 0.0]
    distance = ZeusDBVectorStore._cosine_distance(v1, v2)
    assert 0.8 < distance < 1.2  # Should be ~1.0 for orthogonal vectors


def test_convenience_function_validation() -> None:
    """Test that create_zeusdb_vectorstore validates inputs correctly."""
    import pytest

    from langchain_zeusdb.vectorstores import create_zeusdb_vectorstore

    # Should raise ValueError when embedding is None
    with pytest.raises(ValueError, match="embedding function is required"):
        create_zeusdb_vectorstore(texts=["hello"], embedding=None)
