+++
title = "speed of current laptop"
date = 2018-09-20

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
git rev-parse HEAD
rustc --version
cargo run --release --bin json-benchmark
```

Results:

```
9eae8499c19ecdf3531d72451e0172b56e570c99
rustc 1.29.0 (aa3ca1994 2018-09-11)
    Finished release [optimized + debuginfo] target(s) in 0.04s
     Running `target/release/json-benchmark`
                                DOM                STRUCT
======= serde_json ======= parse|stringify === parse|stringify ===
data/canada.json           9.3ms     5.3ms     3.3ms     4.2ms
data/citm_catalog.json     5.5ms     1.5ms     1.7ms     1.2ms
data/twitter.json          2.1ms     0.9ms     0.9ms     0.8ms

======= json-rust ======== parse|stringify === parse|stringify ===
data/canada.json           6.1ms     3.0ms
data/citm_catalog.json     2.8ms     0.7ms
data/twitter.json          1.2ms     0.5ms

==== rustc_serialize ===== parse|stringify === parse|stringify ===
data/canada.json          14.6ms    33.4ms    19.3ms    48.5ms
data/citm_catalog.json    11.6ms     3.1ms    15.4ms     2.9ms
data/twitter.json          6.3ms     1.5ms     7.9ms     1.4ms
```

[Rust JSON Benchmark]: https://github.com/serde-rs/json-benchmark
