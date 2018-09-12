+++
date = 2018-01-25
title = "Rust week of 2018-01-18"

[taxonomies]
tags = ['Rust']
+++

I did very little Rust on week of 2018-01-11, but [added
\--ignore-uncommitted-repos to mrh].

This week was more active\...

-   I used the fantastic dialoguer for the first time\... so pleasant,
    resulting in much cleaner code for a private project.
-   For [the work project I mentioned some months ago], I added a
    feature to check if certain ports of a remote machine are reachable.
    The bigger part though was it \'forced\' me to refactor the code,
    since the various bits needed checking at different intervals\... in
    my case, as an example, I check port reachability once in 60
    seconds, but would check load average once in 6.

  [added \--ignore-uncommitted-repos to mrh]: https://github.com/tshepang/mrh/commit/0bb76224978fca2324ae7b673472b68033db5a78
  [the work project I mentioned some months ago]: http://tshepang.net/rust-week-of-2017-10-05
