+++
title = "speed of current laptops (part 2)"
date = 2023-01-23

[taxonomies]
tags = ["hardware", "Rust"]
+++

*See [part 1]*

I recently bought a lovely laptop, [Asus Zenbook UM3402].
It replaces a Dell Latitude 5521,
partly due to bad battery life (about 2 hours),
which is a pain since the country (South Africa) faces power outages as long as 4 hours.

To check performance, I used  [Rust JSON Benchmark]:

```
git clone https://github.com/serde-rs/json-benchmark
cd json-benchmark
git checkout de23484ca078b9756e6e35f2a7a3fd1e806769bc
rustup override set 1.66
cargo build --release
cargo run --quiet --release --bin json-benchmark
```

Results for the Zenbook:

```
...
   Compiling json-benchmark v0.0.1 (/tmp/json-benchmark)
    Finished release [optimized + debuginfo] target(s) in 34.64s
                                    DOM                  STRUCT
======= serde_json ======= parse|stringify ===== parse|stringify ====
data/canada.json         410 MB/s   530 MB/s   630 MB/s   470 MB/s
data/citm_catalog.json   700 MB/s   850 MB/s  1230 MB/s  1090 MB/s
data/twitter.json        430 MB/s  1080 MB/s   820 MB/s  1160 MB/s

==== rustc_serialize ===== parse|stringify ===== parse|stringify ====
data/canada.json         220 MB/s   110 MB/s   170 MB/s    77 MB/s
data/citm_catalog.json   330 MB/s   260 MB/s   210 MB/s   280 MB/s
data/twitter.json        170 MB/s   460 MB/s   120 MB/s   480 MB/s

======= simd-json ======== parse|stringify ===== parse|stringify ====
data/canada.json         530 MB/s   600 MB/s   640 MB/s
data/citm_catalog.json  1550 MB/s  1080 MB/s  2150 MB/s
data/twitter.json       1400 MB/s  1600 MB/s  1350 MB/s
```

Results for the Latitude:

```
   Compiling json-benchmark v0.0.1 (/tmp/json-benchmark)
    Finished release [optimized + debuginfo] target(s) in 28.30s
                                DOM                  STRUCT
======= serde_json ======= parse|stringify ===== parse|stringify ====
data/canada.json         510 MB/s   590 MB/s   710 MB/s   490 MB/s
data/citm_catalog.json   670 MB/s  1000 MB/s  1270 MB/s  1320 MB/s
data/twitter.json        480 MB/s  1240 MB/s   790 MB/s  1270 MB/s

==== rustc_serialize ===== parse|stringify ===== parse|stringify ====
data/canada.json         240 MB/s   110 MB/s   190 MB/s    77 MB/s
data/citm_catalog.json   340 MB/s   290 MB/s   220 MB/s   330 MB/s
data/twitter.json        180 MB/s   550 MB/s   130 MB/s   590 MB/s

======= simd-json ======== parse|stringify ===== parse|stringify ====
data/canada.json         540 MB/s   690 MB/s   620 MB/s
data/citm_catalog.json  1410 MB/s  1230 MB/s  1870 MB/s
data/twitter.json       1420 MB/s  1660 MB/s  1500 MB/s
```

The Zenbook (Ryzen 7 5825U) is a bit slower than the Latitude,
except for the SIMD tests.
I expected the Latitude (i7-11850H) to be a lot faster,
given how hungry it is for battery.

[part 1]: @/speed-of-current-laptops.md
[Asus Zenbook UM3402]: https://www.computermania.co.za/asus-zenbook-14-oled-um3402ya-716512b0w-amd-ryzen-7-16gb-ram-512gb-ssd-jade-black.html
[Rust JSON Benchmark]: https://github.com/serde-rs/json-benchmark
