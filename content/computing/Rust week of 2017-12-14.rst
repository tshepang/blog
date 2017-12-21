Rust week of 2017-12-14
=======================

:date: 2017-12-21
:tags: Rust



Some more work on mrh__:

- A friend did me a nice favor of `creating an Iterator for Crawler`__,
  a task I failed at after 2 attempts... I don't yet truly get Rust lifetimes
- Based on that work, I turned Crawler__ itself into an Iterator
- I added YAML and JSON output; they are behind a compile flag, since
  they bring with them some slow-compiling dependencies, and I don't
  expect the features would be a common need


__ https://crates.io/crates/mrh
__ https://github.com/tshepang/mrh/pull/1
__ https://docs.rs/mrh/0.8.1/mrh/struct.Crawler.html
