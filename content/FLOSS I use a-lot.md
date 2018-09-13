+++
title = "FLOSS I use a-lot"
date = 2018-09-12

[taxonomies]
tags = ['list']
+++

Following are tools I use a lot, but am not necessarily loving...
There is [a separate post] for those.

---

*environment*

- **Debian**: my primary OS, and also my favorite
- [dwm]: simple and clean window management
- [tmux][]: amazingly powerful, though I wish it had less rendering bugs
- **Emacs**: pleasant text editing and file management
- **bash**, and **fish**: the latter is new to me, and still under
  evaluation... it's a far more pretty ui, with a fancy completion
  system that also gets in the way rather often

*software development*

-   **cargo**: primary tool for Rust development
-   **Git**: this one has won the mindshare... using it for work and open source
-   **Mercurial**: slight preference over Git

*work*

Out infrastructure is made up of remote machines that ferry data to
central servers

-   **Docker**: each component of the server runs in a container
-   **salt**: administers the remote machines
-   **VirtualBox**: these remotes can be virtual... great for testing
-   **journalctl** & **sysmtemctl**: these remotes run systemd
-   **Elasticsearch**: the data store

*GUI applications*

-   **Xfce Terminal**
-   **Firefox**
-   [Transmission][]: the only torrent client I have ever used
-   **Nautilus**: decent GUI file manager

*network diagnosis*
-   [vnstat]: nifty network usage viewer
-   **ping**: checks general reachability
-   **mtr**: interactive traceroute tool
-   **netcat**: for checking if tcp ports are reachable

*entertainment*

-   **Quod Libet**: audio player that comes with a very excellent tag
    editor, **Ex Falso**
-   **VLC**: user interface could be a lot better

*miscellaneous tools*

-   **wajig**: acts as pleasant front-end to apt and other
    package management tools;
    [I used to maintain it], and it happens to be the one Debian
    package that makes me a Debian Maintainer (I got upload access
    for it)
-   **apt**: Debian package management
-   **head** and **tail**: included in GNU coreutils suite of tools
-   [less][]: indispensable!
-   **OpenSSH**: duh!
-   [Sudo]: another duh!
-   [Fabric][]: I use it to build and deploy my blogs... it's some
    sort of replacement for shell scripting
-   [youtube-dl][]: I prefer watching videos locally, with VLC
-   [ripgrep]: grep replacement (better speed and ux),
    and the most important non-dev tool written in Rust
-   [Iotop]: nifty I/O usage viewer



  [a separate post]: http://tshepang.net/favorite-floss
  [I used to maintain it]: http://tshepang.net/tagss#wajig-ref
  [Transmission]: http://www.transmissionbt.com
  [dwm]: http://tshepang.net/my-current-desktop-setup
  [tmux]: http://tmux.sourceforge.net
  [less]: http://www.greenwoodsoftware.com/less
  [Fabric]: http://fabfile.org
  [youtube-dl]: http://rg3.github.io/youtube-dl
  [ripgrep]: http://blog.burntsushi.net/ripgrep
  [Sudo]: http://tshepang.net/project-of-note-sudo
  [Iotop]: http://tshepang.net/project-of-note-sudo
  [vnstat]: http://humdi.net/vnstat
