<p align="center" width="100%">
  <h1 align="center">LangChain ZeusDB Integration</h1>
</p>

<!-- badges: start -->

<div align="center">
  <table>
    <tr>
      <td><strong>Meta</strong></td>
      <td>
        <a href="https://pypi.org/project/langchain-zeusdb/"><img src="https://img.shields.io/pypi/v/langchain-zeusdb?label=PyPI&color=blue"></a>&nbsp;
        <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%7C3.11%7C3.12%7C3.13-blue?logo=python&logoColor=ffdd54"></a>&nbsp;
        <a href="https://github.com/zeusdb/langchain-zeusdb/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>&nbsp;
        <a href="https://github.com/ZeusDB"><img src="https://github.com/user-attachments/assets/e140d900-1160-4eaa-85c0-2b3507a5f0f5" alt="ZeusDB"></a>&nbsp;
      </td>
    </tr>
  </table>
</div>

<!-- badges: end -->

A high-performance LangChain integration for ZeusDB, bringing enterprise-grade vector search capabilities to your LangChain applications.
<!-- A high-performance LangChain integration for [ZeusDB](https://zeusdb.com), bringing enterprise-grade vector search capabilities to your LangChain applications.-->

## Features

🚀 **High Performance**
- Rust-powered vector database backend
- Advanced HNSW indexing for sub-millisecond search
- Product Quantization for 4x-256x memory compression
- Concurrent search with automatic parallelization

🎯 **LangChain Native**
- Full VectorStore API compliance
- Async/await support for all operations
- Seamless integration with LangChain retrievers
- Maximal Marginal Relevance (MMR) search

🏢 **Enterprise Ready**
- Structured logging with performance monitoring
- Index persistence with complete state preservation
- Advanced metadata filtering
- Graceful error handling and fallback mechanisms

## Quick Start

### Installation

```bash
pip install -qU langchain-zeusdb
```

### Basic Usage

```python
from langchain-zeusdb import ZeusDBVectorStore
from langchain-openai import OpenAIEmbeddings
from zeusdb import VectorDatabase

# Initialize embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Create ZeusDB index
vdb = VectorDatabase()
index = vdb.create(
    index_type="hnsw",
    dim=1536,
    space="cosine"
)

# Create vector store
vector_store = ZeusDBVectorStore(
    zeusdb_index=index,
    embedding=embeddings
)

# Add documents
from langchain_core.documents import Document

docs = [
    Document(page_content="ZeusDB is fast", metadata={"source": "docs"}),
    Document(page_content="LangChain is powerful", metadata={"source": "docs"}),
]

vector_store.add_documents(docs)

# Search
results = vector_store.similarity_search("fast database", k=2)
print(f"Found {len(results)} results")
```

### Factory Methods

```python
# Create from texts
vector_store = ZeusDBVectorStore.from_texts(
    texts=["Hello world", "Goodbye world"],
    embedding=embeddings,
    metadatas=[{"source": "text1"}, {"source": "text2"}]
)

# Create from documents
vector_store = ZeusDBVectorStore.from_documents(
    documents=docs,
    embedding=embeddings
)
```

## Advanced Features

### Memory-Efficient Setup with Quantization

For large datasets, use Product Quantization to reduce memory usage:

```python
# Create quantized index for memory efficiency
quantization_config = {
    'type': 'pq',
    'subvectors': 8,
    'bits': 8,
    'training_size': 10000
}

vdb = VectorDatabase()
index = vdb.create(
    index_type="hnsw",
    dim=1536,
    space="cosine",
    quantization_config=quantization_config
)

vector_store = ZeusDBVectorStore(
    zeusdb_index=index,
    embedding=embeddings
)
```

### Persistence

Save and load your vector store:

```python
# Save index
vector_store.save_index("my_index.zdb")

# Load index
loaded_store = ZeusDBVectorStore.load_index(
    path="my_index.zdb",
    embedding=embeddings
)
```

### Advanced Search Options

```python
# Similarity search with scores
results = vector_store.similarity_search_with_score(
    query="machine learning",
    k=5
)

# MMR search for diversity
results = vector_store.max_marginal_relevance_search(
    query="AI applications",
    k=5,
    fetch_k=20,
    lambda_mult=0.7  # Balance relevance vs diversity
)

# Search with metadata filtering
results = vector_store.similarity_search(
    query="database performance",
    k=3,
    filter={"source": "documentation"}
)
```

### As a Retriever

```python
# Convert to retriever for use in chains
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.8}
)

# Use in a chain
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)

answer = qa_chain.run("What is ZeusDB?")
```

## Async Support

All operations support async/await:

```python
# Async operations
await vector_store.aadd_documents(documents)
results = await vector_store.asimilarity_search("query", k=5)
await vector_store.adelete(ids=["doc1", "doc2"])
```

## Monitoring and Observability

### Performance Monitoring

```python
# Get index statistics
stats = vector_store.get_zeusdb_stats()
print(f"Index size: {stats.get('vector_count', 0)} vectors")

# Benchmark search performance
performance = vector_store.benchmark_search_performance(
    query_count=100,
    max_threads=4
)
print(f"Search QPS: {performance.get('parallel_qps', 0)}")

# Check quantization status
if vector_store.is_quantized():
    progress = vector_store.get_training_progress()
    print(f"Quantization training: {progress:.1f}% complete")
```

### Enterprise Logging

The integration includes structured logging for production monitoring:

```python
import logging

# Configure logging to see performance metrics
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("langchain_zeusdb")

# Operations are automatically logged with:
# - Duration measurements
# - Error context
# - Operation metadata
```

## Configuration Options

### Index Parameters

```python
vdb = VectorDatabase()
index = vdb.create(
    index_type="hnsw",           # Index algorithm
    dim=1536,                    # Vector dimension
    space="cosine",              # Distance metric: cosine, l2, l1
    m=16,                        # HNSW connectivity
    ef_construction=200,         # Build-time search width
    expected_size=100000,        # Expected number of vectors
    quantization_config=None     # Optional quantization
)
```

### Search Parameters

```python
results = vector_store.similarity_search(
    query="search query",
    k=5,                         # Number of results
    ef_search=None,              # Runtime search width (auto if None)
    filter={"key": "value"}      # Metadata filter
)
```

## Error Handling

The integration includes comprehensive error handling:

```python
try:
    results = vector_store.similarity_search("query")
except Exception as e:
    # Graceful degradation with logging
    print(f"Search failed: {e}")
    # Fallback logic here
```

## Requirements

- **Python**: 3.10 or higher
- **ZeusDB**: 0.0.8 or higher
- **LangChain Core**: 0.3.74 or higher

## Installation from Source

```bash
git clone https://github.com/zeusdb/langchain-zeusdb.git
cd langchain-zeusdb/libs/zeusdb
pip install -e .
```

## Development

```bash
# Install with test dependencies
pip install -e ".[test]"

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=langchain_zeusdb

# Lint code
ruff check .
ruff format .

# Type checking
mypy .
```

## Performance Benchmarks

In internal benchmarks, ZeusDB has demonstrated exceptional performance for large-scale vector search workloads.

| Operation | Performance | Notes |
|-----------|-------------|-------|
| Index Creation | 1M+ vectors/min | Depends on vector dimension |
| Search Latency | <1ms | Sub-millisecond for most queries |
| Memory Usage | 50-90% reduction | With Product Quantization |
| Concurrent QPS | 10,000+ | Multi-threaded search |

⚠️ Note: These figures represent internal benchmark results under specific test conditions. Actual performance may vary depending on hardware, vector dimensions, dataset size, and workload characteristics.

## Use Cases

- **RAG Applications**: High-performance retrieval for question answering
- **Semantic Search**: Fast similarity search across large document collections
- **Recommendation Systems**: Vector-based content and collaborative filtering
- **Embeddings Analytics**: Analysis of high-dimensional embedding spaces
- **Real-time Applications**: Low-latency vector search for production systems

## Compatibility

### LangChain Versions
- **LangChain Core**: 0.3.74+
- **LangChain Community**: Compatible with all versions
- **LangSmith**: Full tracing and monitoring support

### Distance Metrics
- **Cosine**: Default, normalized similarity
- **Euclidean (L2)**: Geometric distance
- **Manhattan (L1)**: City-block distance

### Embedding Models
Compatible with any embedding provider:
- OpenAI (`text-embedding-3-small`, `text-embedding-3-large`)
- Hugging Face Transformers
- Cohere Embeddings
- Custom embedding functions

## Support

- **Documentation**: [docs.zeusdb.com](https://docs.zeusdb.com)
- **Issues**: [GitHub Issues](https://github.com/zeusdb/langchain-zeusdb/issues)
- **Discussions**: [GitHub Discussions](https://github.com/zeusdb/langchain-zeusdb/discussions)
- **Email**: contact@zeusdb.com

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

---

*Making vector search fast, scalable, and developer-friendly.*
