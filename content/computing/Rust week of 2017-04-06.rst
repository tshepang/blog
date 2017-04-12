Rust week of 2017-04-06
=======================

:date: 2017-04-13
:tags: Rust


I enjoyed working with probor__,
which is a protocol built on top of CBOR data format.
I made `a submission`__ to fix the example in the README,
using the code in `examples/ directory`__.
I managed to turn JSON to CBOR on one side of a TCP socket,
and decode it back to JSON on the other side (using `serde_json`__).
I failed, however, transporting that CBOR data over MQTT
(using the oh-so-complex mqtt-rs__).


__ https://github.com/tailhook/probor
__ https://github.com/tailhook/probor/pull/6
__ https://github.com/tailhook/probor/tree/master/rust/examples
__ https://github.com/serde-rs/json
__ https://github.com/zonyitoo/mqtt-rs
