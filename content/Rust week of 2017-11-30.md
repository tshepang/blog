+++
date = 2017-12-09
title = "Rust week of 2017-11-30"
[taxonomies]
tags = ['Rust']
+++

Like last week, I did some more work on [mrh][]:

-   Replace colored with ansi_term (I prefer the API, and the latter
    was already a dependency of something else)
-   Remove [follow_symlinks] feature (caused weird behavior)
-   Use [Path.strip_prefix] instead of a custom solution

For work (lucky me), I did a small tool that converts data from a CSV
file containing network ports and their descriptions to a format that
[logstash] can use:

-   I used [csv] crate first time, an experience made pleasant by serde
-   I also used [ordermap] first time, chosen because I care for output
    to match order in csv source file
-   Another first was [tera], and its immaturity surprised me

  [mrh]: https://crates.io/crates/mrh
  [follow_symlinks]: https://docs.rs/walkdir/2.0.1/walkdir/struct.WalkDir.html#method.follow_links
  [Path.strip_prefix]: https://doc.rust-lang.org/std/path/struct.Path.html#method.strip_prefix
  [logstash]: https://www.elastic.co/products/logstash
  [csv]: https://crates.io/crates/ordermap
  [ordermap]: https://crates.io/crates/csv
  [tera]: https://crates.io/crates/tera
