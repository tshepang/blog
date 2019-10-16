+++
title = "Rust week of 2017-04-06"
date = 2017-04-13

[taxonomies]
tags = ['Rust']
+++

I enjoyed working with [probor], which is a protocol built on top of
CBOR data format.
I managed to turn JSON
to CBOR on one side of a TCP socket, and decode it back to JSON on the
other side (using [serde_json]). I failed, however, transporting that
CBOR data over MQTT (using the oh-so-complex [mqtt-rs]).

[probor]: https://github.com/tailhook/probor
[serde_json]: https://github.com/serde-rs/json
[mqtt-rs]: https://github.com/zonyitoo/mqtt-rs
