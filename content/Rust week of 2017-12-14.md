+++
date = 2017-12-21
title = "Rust week of 2017-12-14"

[taxonomies]
tags = ['Rust']
+++

Some more work on [mrh][]:

-   A friend did me a nice favor of [creating an Iterator for Crawler],
    a task I failed at after 2 attempts\... I don\'t yet truly get Rust
    lifetimes
-   Based on that work, I turned [Crawler] itself into an Iterator
-   I added YAML and JSON output; they are behind a compile flag, since
    they bring with them some slow-compiling dependencies, and I don\'t
    expect the features would be a common need

  [mrh]: https://crates.io/crates/mrh
  [creating an Iterator for Crawler]: https://github.com/tshepang/mrh/pull/1
  [Crawler]: https://docs.rs/mrh/0.8.1/mrh/struct.Crawler.html
