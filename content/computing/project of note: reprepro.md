---
date: '2012-05-11'
tags: 'Debian, project-of-note'
title: 'project of note: reprepro'
---

I have given kudos to [reprepro][] [twice][] [before], and though those
2 posts are actually outdated, I still keep a custom repository, a
subset of the official repository of a specific arch, but only of
packages that I ever install.

------------------------------------------------------------------------

Every once in a while, I run this command:

    $ reprepro -vv --basedir ~/.custom_repo/ includedeb tshepang \
    /var/cache/apt/archives/*deb

What it does is add packages that are stored by the Debian package
management system (located in `/var/cache/apt/archives`) to the custom
repository (located in `~/.custom_repo`). That ensures that I only keep
packages that matter to me for any later install.

Note that `tshepang` is the name of the repository. It\'s an unofficial
equivalent of `testing` and `unstable`.

Another command that I sometimes run, though less frequently, is:

    $ reprepro -vv --basedir ~/.custom_repo/ includedeb tshepang \
    /var/cache/apt/archives/*deb

This one is used to help keep the repository fresh. Check out [this
post] for an explanation.

Even less frequently, it happens that some package files are no longer
referenced (i.e. not found in `Package.gz`) for some reason. Here\'s
handy command to display them:

    $ reprepro --basedir ~/.custom_repo dumpunreferenced

And here\'s another that actually gets rid of them:

    $ reprepro --basedir ~/.custom_repo deleteunreferenced

  [reprepro]: http://mirrorer.alioth.debian.org/
  [twice]: http://tshepang.net/reprepro-saved-my-live
  [before]: http://tshepang.net/what-i-do-after-debian-installation
  [this post]: http://tshepang.net/removing-obsolete-packages-from-a-local-debian-repository
