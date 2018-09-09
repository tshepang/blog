+++
date = 2011-02-09
tags = ['Debian', 'Python']
title = "comparing Debian repositories"
+++

If you got two Debian repositories, it\'s quite easy to check the
differences in package versions between them:

``` {.sourceCode .python}
import os
import gzip
import apt_pkg

repo1 = "~/.repo_custom/dists/cache/main/binary-i386/Packages.gz"
repo1 = os.path.expanduser(repo1)
repo1 = apt_pkg.TagFile(gzip.open(repo1, "rb"))
repo1 = dict([(pkg["Package"], pkg["Version"]) for pkg in repo1])

repo2 = "~/.repo_bin/dists/squeeze/main/binary-i386/Packages.gz"
repo2 = os.path.expanduser(repo2)
repo2 = apt_pkg.TagFile(gzip.open(repo2, "rb"))
repo2 = dict([(pkg["Package"], pkg["Version"]) for pkg in repo2])

apt_pkg.init_system()
for pkg in repo1:
    if pkg in repo2:
        vc = apt_pkg.version_compare(repo1[pkg], repo2[pkg])
        if vc > 0:
            print("{0}t{1}t({2})".format(repo1[pkg], repo2[pkg], pkg))
```

The line `import apt_pkg` implies that **python3-apt** is installed.

Here\'s a snippet of what the output will look like:

    2.32.1-2    2.28.1-6    (gconf-defaults-service)
    0.23.0-1    0.21.1-1    (pylint)
    2.91.5-2    2.30.2-2    (libgnomekbd-common)
    0.21.2-1    0.16.4-1    (libpixman-1-dev)
    2.91.7-1    2.30.1-2    (nautilus)
    0.9.22-1    0.9.21-3    (pulseaudio-utils)

Here, we get a display of package versions where the repo1 (custom repo
in this case) is greater than repo2 version. To do it the other way
around, use the `<` character in the comparison line, `if vc > 0`.

further reading
===============

-   modules: [gzip], [os]
-   3rd party library: [apt\_pkg]

  [gzip]: http://docs.python.org/library/gzip
  [os]: http://docs.python.org/library/os
  [apt\_pkg]: http://apt.alioth.debian.org/python-apt-doc/library/apt_pkg.html
