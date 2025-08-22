# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] - 2025-08-22

### Added
- Getting Started section with optional OpenAI setup instructions
- Comprehensive async examples for both Python scripts and Jupyter notebooks
- Expected results sections for all code examples to help users verify correct behavior
- Detailed persistence section explaining what gets saved (vectors, metadata, HNSW graph, quantization state)
- Enhanced Advanced Search Options with MMR, metadata filtering, and retriever integration
- Documentation links throughout for quantization, persistence, metadata filtering, and logging
- Complete docstring usage example with all necessary imports

### Changed
- Restructured README flow from installation → getting started → basic usage → advanced features
- Updated "As a Retriever" section to use modern LCEL syntax with langchain-core only
- Enhanced factory methods section to show they create and populate stores in one step
- Updated enterprise logging section to accurately reflect ZeusDB's built-in capabilities rather than simple LangChain integration

### Fixed
- Corrected stats API usage from `vector_count` to `total_vectors` key
- Updated async examples to handle both script and notebook environments correctly

### Removed
- Inaccurate enterprise logging description in README that suggested it was just a LangChain integration feature

---

## [0.1.0] - 2025-08-21

### Added
- Initial release of langchain-zeusdb package
- Full LangChain VectorStore API compliance with all required methods:
  - `add_documents()` and `add_texts()` for document ingestion
  - `similarity_search()` and `similarity_search_with_score()` for vector search
  - `get_by_ids()` for document retrieval by ID
  - `delete()` for document removal
  - `embeddings` property for embedding function access
- Complete async support for all operations using `run_in_executor`
- Advanced search capabilities:
  - Maximal Marginal Relevance (MMR) search with proper diversity scoring
  - Search by vector directly with automatic coercion (lists, tuples, NumPy arrays)
  - Automatic score normalization for all distance metrics (cosine, L2, L1)
  - Enhanced similarity search with fallback mechanisms for LangChain test compliance
- Enterprise-grade structured logging with performance monitoring
  - Operation context tracking with duration measurements
  - Detailed error logging with operation context
  - Graceful fallback to standard logging when enterprise logging unavailable
  - Performance metrics logging (embedding time, search time, operation success rates)
- Factory methods for easy instantiation:
  - `from_texts()` for creating from text lists
  - `from_documents()` for creating from LangChain Documents
  - Automatic index creation with dimension detection
  - Built-in embedding dimension validation
- ZeusDB-specific utility methods:
  - `get_zeusdb_stats()` for index statistics
  - `get_quantization_info()` for quantization status
  - `save_index()` and `load_index()` for persistence
  - `benchmark_search_performance()` for performance testing
  - `get_training_progress()` for quantization training status
  - `get_vector_count()` for index size monitoring
  - `is_quantized()` and `can_use_quantization()` for quantization status checks
  - `get_storage_mode()` for storage configuration information
- Comprehensive error handling with graceful degradation
  - Automatic fallback to broader search when insufficient results found
  - Robust vector coercion with detailed error logging and warnings
  - Safe handling of missing or corrupted index data
- Support for ZeusDB's advanced features:
  - Product Quantization for memory optimization (4x-256x compression)
  - Index persistence with complete state preservation
  - Metadata filtering with advanced operators
  - Multiple distance metrics (cosine, L2, L1)
  - Configurable HNSW parameters (M, ef_construction, ef_search)
- Type safety with comprehensive type hints and runtime validation
- Backwards compatibility alias (`ZeusDBLangChain`) for migration
- Comprehensive test suite with LangChain integration tests
- Full documentation with Jupyter notebook examples
- Support for Python 3.10, 3.11, and 3.12

---

## [Unreleased]

### Added
<!-- Add new features here -->

### Changed
<!-- Add changed behavior here -->

### Fixed
<!-- Add bug fixes here -->

### Removed
<!-- Add removals/deprecations here -->

---