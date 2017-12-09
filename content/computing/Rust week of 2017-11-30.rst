Rust week of 2017-11-30
=======================

:date: 2017-12-09
:tags: Rust


Like last week, I did some more work on mrh__:

- Replace colored with ansi_term (I prefer the API, and the latter was
  already a dependency of something else)
- Remove `follow_symlinks`__ feature (caused weird behavior)
- Use `Path.strip_prefix`__ instead of a custom solution

For work (lucky me), I did a small tool that converts data from a CSV
file containing network ports and their descriptions to a format that
logstash__ can use:

- I used csv__ crate first time, an experience made pleasant by serde
- I also used ordermap__ first time, chosen because I care for output to match
  order in csv source file
- Another first was tera__, and its immaturity surprised me


__ https://crates.io/crates/mrh
__ https://docs.rs/walkdir/2.0.1/walkdir/struct.WalkDir.html#method.follow_links
__ https://doc.rust-lang.org/std/path/struct.Path.html#method.strip_prefix
__ https://www.elastic.co/products/logstash
__ https://crates.io/crates/ordermap
__ https://crates.io/crates/csv
__ https://crates.io/crates/tera
