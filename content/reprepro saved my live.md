+++
date = 2008-12-12
title = "reprepro saved my live"

[taxonomies]
tags = ['Debian']
+++

Much of this is obsolete: I no longer build my own Debian packages.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

That\'s a joke title, but [that fabulous tool] really did help me a lot.
When doing package builds, all I need to run is the following after a
build:

``` {.sourceCode .sh}
$ rm *udeb
$ reprepro --basedir ~/.repo_directory includedeb sid *deb
$ sudo apt-get update
```

The first command removes debian-installer packages which I don\'t need,
the second takes the remaining packages and adds them into the
reprepro-managed Debian repository while also making them available in
the Packages file, and the third updates the system\'s apt database in
order to pick up the changes. Also, if I want to get rid of something
from the repo, all I do is:

    $ reprepro --basedir ~/.repo_directory removesrc sid glibc

I don\'t know why anyone would love to remove glibc binary packages, but
it\'s that simple.

Achieving this used to be painful before I discovered reprepro, for I
did the whole thing manually, which was not scalable since old packages
were sitting rotting in the repo, making it grow beyond 30GB (it now is
about 10GB). This also meant that I ran \'apt-ftparchive packages\' on
the entire .debs each time I wanted an updated Packages file, and that
was dozens of minutes of heavy I/O. This painful life has been going on
for a number of months, and am stupid that I didn\'t search harder for a
better solution.

Before doing things this way, I was making use of the nifty [APTonCD],
but it started to become unusable due to excessive memory consumption
after some system updates. It\'s not clear where the bug lies, nor do I
know if it\'s a known problem, which I didn\'t report because I was
using Ubuntu\'s package, a much improved and re-written 0.1.98, as
opposed to Debian\'s \'bug-free\' 0.1 (though I later discovered the bug
to exist when running the package in Ubuntu 8.10 too).

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

[an update on how I do things now]

  [that fabulous tool]: http://mirrorer.alioth.debian.org/
  [APTonCD]: http://aptoncd.sourceforge.net/
  [an update on how I do things now]: http://tshepang.net/my-debian-package-management-setup
