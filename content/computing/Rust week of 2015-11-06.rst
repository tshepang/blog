Rust week of 2015-11-06
=======================

:date: 2015-11-10
:tags: Rust


I made some `small improvements`__ to rustc-serialize docs.  I also
looked at parsing JSON, and `it doesn't look too bad`__.  I am mostly
interested in the ``from_str`` method, and was surprised to find that
it's pretty much the same as that of (the more modern) `serde_json`__.


__ https://github.com/rust-lang-nursery/rustc-serialize/pull/136
__ https://doc.rust-lang.org/num/rustc_serialize/json/index.html
__ https://serde-rs.github.io/serde/serde_json/serde_json
