+++
title = "speed of current laptop"
date = 2019-03-01

[taxonomies]
tags = ["hardware", "Rust"]
+++

Few weeks ago I got me a new laptop (battery circuitry of my old Asus
UX305 got fried).  This one is Asus UX410, with Intel i7-8550U
processor and 16GB of DDR4 RAM.

To check performance, I use [Rust JSON Benchmark]:

```
git clone https://github.com/serde-rs/json-benchmark
cd json-benchmark
git checkout ac6076683bb73e1e82181e4928d7bc520db9aaa7
rustup default 1.33.0
cargo run --release --bin json-benchmark
```

Results:

```
ac6076683bb73e1e82181e4928d7bc520db9aaa7
DOM                  STRUCT
======= serde_json ======= parse|stringify ===== parse|stringify ====
data/canada.json         260 MB/s   430 MB/s   620 MB/s   330 MB/s
data/citm_catalog.json   410 MB/s   410 MB/s   950 MB/s   600 MB/s
data/twitter.json        270 MB/s   640 MB/s   590 MB/s   740 MB/s

======= json-rust ======== parse|stringify ===== parse|stringify ====
data/canada.json         430 MB/s   810 MB/s
data/citm_catalog.json   710 MB/s   520 MB/s
data/twitter.json        470 MB/s   700 MB/s

==== rustc_serialize ===== parse|stringify ===== parse|stringify ====
data/canada.json         180 MB/s    70 MB/s   130 MB/s    53 MB/s
data/citm_catalog.json   200 MB/s   200 MB/s   140 MB/s   230 MB/s
data/twitter.json        110 MB/s   390 MB/s    94 MB/s   420 MB/s
```

[Rust JSON Benchmark]: https://github.com/serde-rs/json-benchmark
