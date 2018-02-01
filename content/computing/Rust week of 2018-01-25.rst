Rust week of 2018-01-25
=======================

:date: 2018-02-01
:tags: Rust



Continuing on `a work project`__ I mentioned months ago,
I had `a failure related to cross-building pnet`__,
a library I was using to get network interfaces.
As a side note, `the fault was in the build process`__,
not the crate itself.
I tried a few others as replacement:

- getaddrs can't find ip address, and it's abandoned according to the author,
  in favor of `nix crate`__

- interfaces also fails to cross build, and I forgot that I actually
  tried it before, and was the reason I moved to pnet in the first place

- systemstat works, and I already use it for a few things:

  + load average
  + memory usage
  + uptime

  So, that's one less dependency, though I do wish this functionality
  was available from a more pleasant API... systemstat is ugly.

As a general note,
I wish more people took the effort to state in the
README if their software is abandoned,
perhaps with mentions of alternatives.


__ http://tshepang.net/rust-week-of-2017-10-05
__ https://github.com/libpnet/libpnet/issues/309
__ https://github.com/japaric/cross/issues/39
__ https://crates.io/crates/nix
