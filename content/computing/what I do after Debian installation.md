+++
date = 2012-11-10
tags = ['Debian']
title = "what I do after Debian installation"
+++

I think anyone who has never done any OS install before can install
Debian without any issue at all, provided they will not be doing any
partitioning. It is that easy.

As for me, I do a lot more installations than the average person, so I
semi-automate the setup process with the help of this script:

::: {.sourcecode}
sh

\#!/bin/bash

\# some convenience shopt -s expand\_aliases source
\~/nna/conf/bash\_aliases

\# config files sudo cp \~/nna/conf/sources.list /etc/apt sudo cp
\~/nna/conf/sudoers /etc

\# APT sudo apt-get update sudo apt-get \--allow-unauthenticated upgrade
sudo apt-get \--allow-unauthenticated dist-upgrade sudo apt-get
\--allow-unauthenticated install devscripts debhelper build-essential
python3-apt gpm

\# wajig (cd \~/src/wajig && iiwajig) ibase && inondebian && itracker &&
icpython && ipurge

\# for Tracker sudo sh -c \"echo
\'fs.inotify.max\_user\_watches=100000\' \>\> /etc/sysctl.conf\"

\# so I can share via a webserver, or easily access from browser sudo ln
-s \~/.custom\_repo /var/www/custom\_repo
:::

Contents of Debian repository list file:

``` {.sourceCode .sh}
$ cat /etc/apt/sources.list
deb file:/home/wena/.custom_repo tshepang main
deb http://debian.mirror.ac.za/debian wheezy main contrib non-free
```

The `tshepang` codename refers to my custom repository, the one managed
by [reprepro].

Contents of **sudo** setup file:

``` {.sourceCode .sh}
$ sudo cat /etc/sudoers
Defaults env_reset
Defaults mail_badpass
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
root     ALL=(ALL) ALL
%sudo    ALL=(ALL) ALL
Defaults !tty_tickets
Defaults timestamp_timeout=100
```

The one change from default **sudo** setup is so that each bash session
can inherit sudo powers from another. It\'s one case where I trade
[security] for convenience. Another such case is increasing the
ask-for-password timeout to 100 minutes, instead of the default 15
minutes.

And then these aliases, which point to scripts that install some
packages:

-   `ibase`: basic stuff I got to have, stuff like the components I use
    for my desktop apps, some CLI tools, and some documentation
-   `inondebian`: packages that aren\'t part of Debian, e.g. stuff from
    external repositories, or nonm-free stuff from Debian repos
-   `itracker`: I always run the git version of [Tracker], so these
    tools help me build it
-   `ipurge`: stuff that was installed as Recommends dependencies of the
    above (e.g. `gnome-bluetooth`) or during Debian installation (e.g.
    `vim`), but that I won\'t use

The symbolic links is so that those I share a network with (LAN) can
have easy web browser access to some stuff on my machine.

  [reprepro]: http://tshepang.net/project-of-note-reprepro
  [security]: http://ask.debian.net/questions/how-to-have-sudo-powers-shared-between-different-bash-sessions
  [Tracker]: http://projects.gnome.org/tracker/