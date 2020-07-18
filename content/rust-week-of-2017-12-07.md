+++
title = "Rust week of 2017-12-07"
date = 2017-12-14

[taxonomies]
tags = ['Rust']
+++

Some more work on [mrh][]:

- Use ordermap for repeatable output
- Turn into a library (backed by the command-line tool), which is a
  first for me (libs are more hard than apps, and helpfully force one
  to do a better design).

I experienced some failures too:

- I looked to using [termcolor] (used by ripgrep and cargo, and [may
  replace termcolor in clap]), but found it too hard to use... API
  not as pleasant
- I also failed to turn output into an iterator (instead of Vec)


[mrh]: https://crates.io/crates/mrh
[may replace termcolor in clap]: https://github.com/kbknapp/clap-rs/issues/836
[termcolor]: https://crates.io/crates/termcolor
