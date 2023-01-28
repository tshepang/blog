+++
title = "my Debian package management setup"
date = 2010-09-28

[taxonomies]
tags = ['Debian']
+++

Much of this is obsolete: I no longer use `debmirror` and no longer keep
the entire binary repository of i386 arch.

---

There's a useful tool in Debian named debmirror. It's function is to
create and manage a partial copy of an official Debian repository, and I
use it to create 2 repos:

-   an entire i386 Debian repo for [Squeeze]
-   an entire source Debian repo for [Squeeze]

How this works is that I'd run the following command (an example for
the source repo):

    /usr/bin/debmirror
     --verbose
     --progress
     --host=ftp.sun.ac.za
     --passive
     --dist=squeeze
     --root=ftp/debian
     --section=main
     --method=ftp
     --arch=none
     /home/wena/.repo_src

(look at debmirror's manpage to see what all those options mean)

The result is that I'll be having ~30GB of Debian locally (for a
comparison, see [total Debian archive size]).

That's a lot of data, most of which I'll never use, but:

-   I do this as a matter of convenience; I want to be able to install
    anything when I'm having a fresh machine, and internet access is
    not yet fast and cheap in South Africa.
-   I also like to mess around with the packaging system, deleting and
    reinstalling packages on a whim, and I don't want to be waiting for
    some file to download when I do that kind of tinkering.

Now, since it's ridiculous to do this every time just to have the most
recent packages (a weekly update is maybe >1GB of data), I've found
another wonderful tool named reprepro. It's purpose is to create a
custom (unofficial) Debian repo. It's a far more advanced tool than
debmirror, and I think it can do what debmirror does (but I don't yet
care to learn how).

Moving on, here's the relevant entries from my /etc/apt/sources.list
file:

```sh
# local repos (debmirror)
deb file:/home/wena/.repo_bin sid main
deb-src file:/home/wena/.repo_src sid main

# local repo (reprepro)
deb file:/home/wena/.repo_local cache main

# remote repo
deb ftp://ftp.sun.ac.za/ftp/debian/ sid main non-free contrib
```

So, what I do on a semi-regular basis is run:

    wajig update && wajig upgrade

The newly-updated packages are stored in a cache so that a reinstall
doesn't have to fetch from network again. After this I run:

    reprepro -vv --basedir ~/.repo_local includedeb cache /var/cache/apt/archives/*deb

This updates the local reprepro repo and after which I can then remove
the cached packages:

    wajig clean

I do that because they are now available in my reprepro-managed repo.
That now means that I got a massive mirror managed by debmirror and a
smaller one managed by reprepro, and I have these on an external drive
for in case I want to install Debian anywhere. What else my reprepro
repo has is some other packages like **skype** and **oracle-xe**, as
well as some odd packages from [Debian Experimental].

Not so simple I guess... but works so well for my needs.

[Squeeze]: http://www.debian.org/releases/squeeze/
[total Debian archive size]: http://www.debian.org/mirror/size
[Debian Experimental]: http://wiki.debian.org/DebianExperimental
