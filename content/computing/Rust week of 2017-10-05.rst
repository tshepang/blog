---
date: '2017-10-13'
tags: Rust
title: 'Rust week of 2017-10-05'
---

[Continuing with the work project], I replaced the [interfaces] library
with [pnet], a weird concoction of various network functionality in one
ugly mess, but I did it because the order of the network interfaces it
presents does not randomly change (the project is UI that presents
various bits of info about the boxes that we sell, some of which is
network-related), unlike is the case with *interfaces*. It is also
comforting that the library has more users ([one] vs. [eight] at time of
writing).

  [Continuing with the work project]: http://tshepang.net/rust-weeks-of-2017-09-14-to-2017-09-28
  [interfaces]: https://github.com/andrew-d/interfaces-rs
  [pnet]: https://github.com/libpnet/libpnet
  [one]: https://crates.io/crates/interfaces/reverse_dependencies
  [eight]: https://crates.io/crates/pnet/reverse_dependencies
