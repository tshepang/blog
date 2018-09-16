+++
date = 2012-02-21
title = "removing obsolete packages from a local Debian repository"
[taxonomies]
tags = ['Debian']
+++

background info
===============

Bandwidth in South Africa is neither readily-available nor cheap, so
whenever I fetch and install Debian packages (e.g. `apt-get upgrade`), I
also keep them in a local custom repository. I use a great tool named
[reprepro] for this, and this is the command I use to update that
repository, given the location of the fresh package files:

    $ reprepro -vv --basedir ~/.custom_repo/ includedeb tshepang /var/cache/apt/archives/*deb

What's nice about the command is that, if there is an older version of
the pacakge I'm adding, it gets replaced, and the package index is
update accordingly.

and now to the topic at hand
============================

I run that command more or less regularly, but very often the repository
accumulates some junk:

-   If a package gets renamed, reprepro has no way of knowing (at least
    as far as my setup goes). One notable case of this is Debian
    kernels, whose names match the major release versions (e.g.
    `linux-image-3.1.0-1-686-pae` becomes `linux-image-3.2.0-1-686-pae`
    when a new upstream release gets packaged). Lots other packages
    change names, and very often, for a variety of reasons (Debian is a
    little chaotic, often out of necessity, and it's amazing that its
    developers keep it so damn stable given all this change).
-   If I add a package from an external repository or that I converted
    from an rpm, reprepro has no way of knowing that fact. Now if I stop
    using that package, it is just a waste of resources (CPU and disk
    usage).

To help with the cleanup, I have written the following simple script:

``` {.sourceCode .python}
#!/usr/bin/env python3

import apt_pkg
import gzip
import subprocess

CUSTOM_REPO = ("/home/wena/.custom_repo/dists/tshepang/main/"
               "binary-i386/Packages.gz")
WHEEZY_REPO = ("/var/lib/apt/lists/ftp.de.debian.org_debian_dists_testing_{}_"
               "binary-i386_Packages")


def main():
    custom_repo = apt_pkg.TagFile(gzip.open(CUSTOM_REPO, "rb"))
    archive_areas = "main contrib non-free".split()
    wheezy_packages = list()
    for archive_area in archive_areas:
        repo = WHEEZY_REPO.format(archive_area)
        repo = apt_pkg.TagFile(gzip.open(repo, "rb"))
        wheezy_packages.extend([pkg["Package"] for pkg in repo])
    for package in custom_repo:
        package_name = package["Package"]
        if package_name not in wheezy_packages:
            cmd = "apt-cache policy " + package_name
            subprocess.call(cmd.split())
            choice = input("remove from cache [Y/n]? ")
            if not choice or choice.lower().startswith("y"):
                cmd = ("reprepro -vv --basedir /home/wena/.custom_repo/ "
                       "remove tshepang " + package_name)
                subprocess.call(cmd.split())

if __name__ == "__main__":
    main()
```

And here's a snippet of its output:

    cx-oracle:
      Installed: 5.1.1-2
      Candidate: 5.1.1-2
      Version table:
     *** 5.1.1-2 0
            500 file:/home/wena/.custom_repo/ tshepang/main i386 Packages
            100 /var/lib/dpkg/status
    remove from cache [Y/n]?

What it does is look for packages which are only available in my custom
reposity, as compared with the one in Wheezy (soon to be Debian 7). It
then prompts me on whether or not to remove it from that custom
repository. Today, it helped me get rid of dozens of junk.

  [reprepro]: http://mirrorer.alioth.debian.org/
