+++
title = "Rust search tools to watch"
date = 2024-06-17

[taxonomies]
tags = ["Rust"]
+++

These are all maintained well:

- [Quickwit]

  - "search engine for log management"
  - built on [Tantivy], an equivalent of [Lucene]
  - search API compatible with that of Elasticsearch

- [Meilisearch]
  - uses LMDB as backing store

- [Spyglass]: search engine that crawls websites and stores them locally

- [Sonic]

  - "a schema-less search backend"
  - uses [RocksDB] as backing store

[Quickwit]: https://github.com/quickwit-oss/quickwit
[Tantivy]: https://github.com/quickwit-oss/tantivy
[Lucene]: https://github.com/apache/lucene
[Meilisearch]: https://github.com/meilisearch/meilisearch
[BonsaiDb]: https://github.com/khonsulabs/bonsaidb
[Nebari]: https://github.com/khonsulabs/nebari
[update]: https://bonsaidb.io/blog/durable-writes
[Sonic]: https://github.com/valeriansaliou/sonic
[RocksDB]: https://github.com/facebook/rocksdb
[Spyglass]: https://github.com/a5huynh/spyglass
