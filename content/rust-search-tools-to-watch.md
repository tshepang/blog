+++
title = "Rust search tools to watch"
date = 2022-04-09

[taxonomies]
tags = ["Rust"]
+++

These are well-maintained and see some heavy use:

- [Quickwit]

  - "search engine for log managment"
  - build on [Tantivy], an equivalent of [Lucene]
  - search API compatible with that of Elasticsearch

- [Meilisearch]

- [BonsaiDb]

  - "document sotre"
  - used [Nebari] as backing store

- [Sonic]:

  - "a schema-less search backend"
  - uses [RocksDB] as backing store

[Quickwit]: https://github.com/quickwit-oss/quickwit
[Tantivy]: https://github.com/quickwit-oss/tantivy
[Lucene]: https://github.com/apache/lucene
[Meilisearch]: https://github.com/meilisearch/meilisearch
[BonsaiDb]: https://github.com/khonsulabs/bonsaidb
[Nebari]: https://github.com/khonsulabs/nebari
[Sonic]: https://github.com/valeriansaliou/sonic
[RocksDB]: https://github.com/facebook/rocksdb
