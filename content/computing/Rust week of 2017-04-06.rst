---
date: '2017-04-13'
tags: Rust
title: 'Rust week of 2017-04-06'
---

I enjoyed working with [probor], which is a protocol built on top of
CBOR data format. I made [a submission] to fix the example in the
README, using the code in [examples/ directory]. I managed to turn JSON
to CBOR on one side of a TCP socket, and decode it back to JSON on the
other side (using [serde\_json]). I failed, however, transporting that
CBOR data over MQTT (using the oh-so-complex [mqtt-rs]).

  [probor]: https://github.com/tailhook/probor
  [a submission]: https://github.com/tailhook/probor/pull/6
  [examples/ directory]: https://github.com/tailhook/probor/tree/master/rust/examples
  [serde\_json]: https://github.com/serde-rs/json
  [mqtt-rs]: https://github.com/zonyitoo/mqtt-rs
