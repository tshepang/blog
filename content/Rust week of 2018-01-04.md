+++
date = 2018-01-11
tags = ['Rust']
title = "Rust week of 2018-01-04"
+++

Some more work on [mrh], I added the ability to check if there are
unpulled commits as well as if there are tags that aren\'t pushed
upstream. The latter is what motivated this work, a feature useful for
work, to avoid forgetting pushing tags. This meant doing the dreaded
work of accessing the remote repo, which is complicated by potentially
having to authenticate, in the case of private repos for example. It was
painful (we need an easier git library), but it works (but so damn
slow). The result is version 0.9.

  [mrh]: https://crates.io/crates/mrh
