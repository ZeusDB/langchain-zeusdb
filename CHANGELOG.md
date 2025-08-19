# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-08

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
- Enterprise-grade structured logging with performance monitoring
  - Operation context tracking with duration measurements
  - Detailed error logging with operation context
  - Graceful fallback to standard logging when enterprise logging unavailable
- Factory methods for easy instantiation:
  - `from_texts()` for creating from text lists
  - `from_documents()` for creating from LangChain Documents
  - Automatic index creation with dimension detection
- ZeusDB-specific utility methods:
  - `get_zeusdb_stats()` for index statistics
  - `get_quantization_info()` for quantization status
  - `save_index()` and `load_index()` for persistence
  - `benchmark_search_performance()` for performance testing
  - `get_training_progress()` for quantization training status
- Comprehensive error handling with graceful degradation
- Support for ZeusDB's advanced features:
  - Product Quantization for memory optimization
  - Index persistence with complete state preservation
  - Metadata filtering with advanced operators
  - Multiple distance metrics (cosine, L2, L1)
- Type safety with comprehensive type hints and runtime validation
- Backwards compatibility alias (`ZeusDBLangChain`) for migration

### Changed
<!-- Add changed behavior here -->

### Fixed
<!-- Add bug fixes here -->

### Removed
<!-- Add removals/deprecations here -->

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