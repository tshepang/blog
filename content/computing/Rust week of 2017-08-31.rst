Rust week of 2017-08-31
=======================

:date: 2017-09-08
:tags: Rust



Week of 2017-08-24 did not really see any Rust activity.
This week, however, I worked on mrh__,
a tool I created in order to look at status of multiple git repos,
to avoid the tedium of navigating to each to check.
The feature I added is checking if committed changes were pushed upstream.
On the way there, I encountered these git2 APIS:

- Branch::wrap__ (submitted `improvement to make doc less misleading`__)
- Branch::upstream__
- Repositoty::head__

I ended up `publishing the tool`__ too,
which is the second time `I've done so`__.


__ https://github.com/tshepang/mrh
__ https://docs.rs/git2/0.6.8/git2/struct.Branch.html#method.wrap
__ https://github.com/alexcrichton/git2-rs/pull/246
__ https://docs.rs/git2/0.6.8/git2/struct.Branch.html#method.upstream
__ https://docs.rs/git2/0.6.8/git2/struct.Repository.html#method.head
__ https://crates.io/crates/mrh
__ https://crates.io/crates/weeks-from-now
