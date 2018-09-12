+++
date = 2013-10-16
title = "easing switching between Git and Mercurial"

[taxonomies]
tags = ['Python', 'VCS']
+++

Each chance I get, I use Mercurial (e.g. personal stuff), and use Git
when I don\'t have much of a choice (e.g. FLOSS and work). That is, I
use both quite a lot, and too often I find myself running commands for
one while on another\'s repository\... error. I therefore decided to
ease the pain my creating [a script] which checks which VCS system I\'m
on, and displays the relevant command.

Some examples of usage:

``` {.sourceCode .sh}
$ cd <hg repo>
$ ./vcs.py --log
hg log --no-merges --patch --stat --verbose
$ cd <git repo>
$ ./vcs.py --log
git log --no-merges --patch --stat
```

Here are the relevant BASH aliases:

``` {.sourceCode .sh}
alias vb='$(~/scripts/vcs.py --branch)'
alias vd='$(~/scripts/vcs.py --diff)'
alias vl='$(~/scripts/vcs.py --log)'
alias vp='$(~/scripts/vcs.py --push)'
alias vs='$(~/scripts/vcs.py --status)'
alias vu='$(~/scripts/vcs.py --pull)'
alias vc='$(~/scripts/vcs.py --commit)'
alias vo='$(~/scripts/vcs.py --checkout)'
alias vr='$(~/scripts/vcs.py --revert)'
```

This makes my life so much easier, since I no longer have to care which
VCS I\'m on, at least for the most common of commands. I am pleased with
self.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

As a sidenote, if you want to cycle between the changesets (Mercurial
term) or Commits (Git term), use the following search term on your pager
(tested with [less], which is Debian/Ubuntu default pager):

    (^changeset)|(^commit)

  [a script]: https://bitbucket.org/tshepang/scripts/src/tip/vcs.py
  [less]: http://www.greenwoodsoftware.com/less
