+++
date = 2017-09-08
title = "Rust week of 2017-08-31"
[taxonomies]
tags = ['Rust']
+++

Week of 2017-08-24 did not really see any Rust activity. This week,
however, I worked on [mrh], a tool I created in order to look at status
of multiple git repos, to avoid the tedium of navigating to each to
check. The feature I added is checking if committed changes were pushed
upstream. On the way there, I encountered these git2 APIS:

-   [Branch::wrap] (submitted [improvement to make doc less misleading])
-   [Branch::upstream]
-   [Repositoty::head]

I ended up [publishing the tool] too, which is the second time [I've
done so].

  [mrh]: https://github.com/tshepang/mrh
  [Branch::wrap]: https://docs.rs/git2/0.6.8/git2/struct.Branch.html#method.wrap
  [improvement to make doc less misleading]: https://github.com/alexcrichton/git2-rs/pull/246
  [Branch::upstream]: https://docs.rs/git2/0.6.8/git2/struct.Branch.html#method.upstream
  [Repositoty::head]: https://docs.rs/git2/0.6.8/git2/struct.Repository.html#method.head
  [publishing the tool]: https://crates.io/crates/mrh
  [I've done so]: https://crates.io/crates/weeks-from-now
