+++
title = "FLOSS I use a-lot"
date = 2020-07-22

[taxonomies]
tags = ['list']
+++


### environment

- **Debian**: my primary OS, and also my favorite
- [dwm]: simple and clean window management
- [tmux]: amazingly powerful terminal multiplexer
- **Emacs**: pleasant text editing and file management
- **fish**: compared to mighty Bash, it is far more pretty,
   and has a far better command completion system

### software development

- **cargo**: central tool for Rust development
- **Git**: this one has won the mindshare

### work

Our infrastructure is made up of remote machines that ferry data to
central servers

- **Docker** & **Docker Compose**: each component of the server runs in a container
- **SaltStack**: administers the remote machines
- **journalctl** & **systemctl**: these remote machines run systemd
- **Elasticsearch**: the data store
- **Ubuntu**: the OS running these remotes, and the server
- **Bash**: default shell on Ubuntu

 ### GUI applications

- **Xfce Terminal**
- **Firefox**
- [Transmission][]: the only torrent client I have ever used
- **Nautilus**: decent GUI file manager

### network diagnosis
- [vnstat]: nifty network usage viewer
- **ping**: checks general reachability
- **mtr**: interactive traceroute tool
- **netcat**: for checking if tcp ports are reachable

### entertainment

- [Quod Libet]: audio player
- **VLC**: user interface could be a lot better
- [miniserve]: file server I use at home for video

### miscellaneous tools

- **wajig**: acts as pleasant front-end to `apt` and other
  package management tools;
  [I used to maintain it], and it happens to be the one Debian
  package that makes me a Debian Maintainer (I got upload access
  for it)
- **apt**: Debian package management
- **apt-cacher-ng**: avoids the need to re-fetch Debian packages when needed for
  additional installs, which helps speed things up, especially for poor connections
- **head** and **tail**: included in GNU coreutils suite of tools
- **OpenSSH**: duh!
- [Sudo]: another duh!
- [youtube-dl][]: I prefer watching videos locally, with VLC
- [Iotop]: nifty I/O usage viewer
- [ripgrep]: a more pleasant `grep`
- [exa]: a more pleasant, more pretty `ls`
- [bat]: a more pleasant, more fancy `cat`, which also supplants `less`
  (though it actually makes use of the latter for paging through long text)
- **top**: a powerful and flexible process viewer, part of [procps suite]


[I used to maintain it]: http://tshepang.net/tags/wajig.md
[Transmission]: http://www.transmissionbt.com
[dwm]: @/my-current-desktop-setup.md
[tmux]: https://github.com/tmux/tmux/wiki
[youtube-dl]: http://rg3.github.io/youtube-dl
[ripgrep]: http://blog.burntsushi.net/ripgrep
[Sudo]: @/project-of-note-sudo.md
[Iotop]: @/project-of-note-sudo.md
[vnstat]: http://humdi.net/vnstat
[exa]: https://the.exa.website
[bat]: https://crates.io/crates/bat
[procps suite]: https://gitlab.com/procps-ng/procps
[Quod Libet]: https://quodlibet.readthedocs.io
[miniserve]: https://github.com/svenstaro/miniserve
