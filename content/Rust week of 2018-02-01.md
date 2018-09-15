+++
date = 2018-02-08
title = "Rust week of 2018-02-01"

[taxonomies]
tags = ['Rust']
+++

I used [serde_rusqlite] for the first time, and thought it was
fantastic, if leveraging the wonderful serde framework. On a related
note, it was kool to discover the [rename_all attribute of serde],
which helps reduce noise. Another attribute that reduces noise is
`[allow(dead_code)]`, which is also handy when using serde.

I did a bunch of work on `--access-remote` option of mrh, fixing bugs
and letting it support usage of ssh-agent. This was inspired by a friend
pushing me to make [an announcement], which I promised would happen
before [2018-02-06 meetup], and something I haven't done before.

  [serde_rusqlite]: https://crates.io/crates/serde_rusqlite
  [rename_all attribute of serde]: https://serde.rs/container-attrs.html#serderenameall--
  [an announcement]: https://www.reddit.com/r/rust/comments/7vb3u7/announcing_mrh_the_multigitrepo_helper
  [2018-02-06 meetup]: https://twitter.com/tshepang_dev/status/960955091296702466
