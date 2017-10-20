Rust week of 2017-10-19
=======================

:date: 2017-10-20
:tags: Rust



I released mrh__ v0.2.0,
which takes into account that when latest upstream git reference does
not match one that's checked out,
it could be that upstream is ahead.
The assumption previously was that local is ahead of upstream,
implying that a push is needed.
The API that helped with this change is `Repository.grapth_ahead_behind`__,
a lovely and unexpected gift (commit__).

I used cargo-outdated__ for the first time... I like.


__ https://crates.io/crates/mrh
__ https://docs.rs/git2/0.6.8/git2/struct.Repository.html#method.graph_ahead_behind
__ https://github.com/tshepang/mrh/commit/fc82fe9890cf3a8033fa78295308d888628caa39
__ https://crates.io/crates/cargo-outdated
