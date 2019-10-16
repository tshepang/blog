+++
title = "Rust week of 2017-10-19"
date = 2017-10-22

[taxonomies]
tags = ['Rust']
+++

I released [mrh] v0.2.0, which takes into account that when latest
upstream git reference does not match one that's checked out, it could
be that upstream is ahead. The assumption previously was that local is
ahead of upstream, implying that a push is needed. The API that helped
with this change is [Repository.grapth_ahead_behind], a lovely and
unexpected gift ([commit]).

I used [cargo-outdated] for the first time... I like.

I also released [tag-helper], whose development was sponsored by
[Panoptix], the company I work for. The tool helps reduce the tedium of
tagging git repos, of which we have a bunch.

[mrh]: https://crates.io/crates/mrh
[Repository.grapth_ahead_behind]: https://docs.rs/git2/0.6.8/git2/struct.Repository.html#method.graph_ahead_behind
[commit]: https://github.com/tshepang/mrh/commit/fc82fe9890cf3a8033fa78295308d888628caa39
[cargo-outdated]: https://crates.io/crates/cargo-outdated
[tag-helper]: https://github.com/panoptix-za/tag-helper
[Panoptix]: https://www.panoptix.co.za/
