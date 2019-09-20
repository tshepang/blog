+++
title = "FLOSS I use a-lot"
date = 2019-09-08
[taxonomies]
tags = ['list']
+++


*environment*

- **Debian**: my primary OS, and also my favorite
- [dwm]: simple and clean window management
- [tmux]: amazingly powerful terminal multiplexer,
  though I am yet to figure out how mouse integration works
- **Emacs**: pleasant text editing and file management
- **fish**: compared to mighty Bash, it is far more pretty,
   and has a far better command completion system

*software development*

- **cargo**: primary tool for Rust development
- **Git**: this one has won the mindshare
- **Mercurial**: slight preference over Git

*work*

Out infrastructure is made up of remote machines that ferry data to
central servers

- **Docker** & **Docker Compose**: each component of the server runs in a container
- **SaltStack**: administers the remote machines
- **journalctl** & **systemctl**: these remotes run systemd
- **Elasticsearch**: the data store
- **Ubuntu**: the OS running these remotes, and the server
- **Bash**: default shell on Ubuntu, this one can hardly be avoided

*GUI applications*

- **Xfce Terminal**
- **Firefox**
- [Transmission][]: the only torrent client I have ever used
- **Nautilus**: decent GUI file manager

*network diagnosis*
- [vnstat]: nifty network usage viewer
- **ping**: checks general reachability
- **mtr**: interactive traceroute tool
- **netcat**: for checking if tcp ports are reachable

*entertainment*

- [Quod Libet]: audio player
- **VLC**: user interface could be a lot better

*miscellaneous tools*

- **wajig**: acts as pleasant front-end to apt and other
  package management tools;
  [I used to maintain it], and it happens to be the one Debian
  package that makes me a Debian Maintainer (I got upload access
  for it)
- **apt**: Debian package management
- **head** and **tail**: included in GNU coreutils suite of tools
- **OpenSSH**: duh!
- [Sudo]: another duh!
- [youtube-dl][]: I prefer watching videos locally, with VLC
- [Iotop]: nifty I/O usage viewer
- [ripgrep]: a more pleasant `grep`
- [exa]: a more pleasant, more pretty `ls`
- [bat]: a more pleasant, more fancy `cat`, which also supplants `less`
- **top**: a powerful and flexible process viewer, part of [procps suite]


[a separate post]: http://tshepang.net/favorite-floss
[I used to maintain it]: http://tshepang.net/tags/wajig
[Transmission]: http://www.transmissionbt.com
[dwm]: http://tshepang.net/my-current-desktop-setup
[tmux]: https://github.com/tmux/tmux/wiki
[youtube-dl]: http://rg3.github.io/youtube-dl
[ripgrep]: http://blog.burntsushi.net/ripgrep
[Sudo]: http://tshepang.net/project-of-note-sudo
[Iotop]: http://tshepang.net/project-of-note-sudo
[vnstat]: http://humdi.net/vnstat
[exa]: https://the.exa.website
[bat]: https://crates.io/crates/bat
[procps suite]: https://gitlab.com/procps-ng/procps
[Quod Libet]: https://quodlibet.readthedocs.io
