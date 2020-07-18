+++
date = 2008-09-28
title = "enjoying net connection at home, finally"
[taxonomies]
tags = ['untagged']
+++

After suffering with being forced to access the net on Windows XP [for
over 2 weeks], I'm glad things turned out as I envisioned for I managed
to get my device working on Debian [with a lot of help]. Here's what
went into my /etc/wvdial.conf:

I had to run `sudo modprobe usbserial vendor=0x1d09 product=0x4000` and
then `sudo wvdial neotel` afterwards and then I lived happily for
long...

Now why is XP so uncomfortable? I'm used to many of the conveniences of
Debian that are absent in XP or I'm not motivated to find replacements
for stuff like workspaces, copy-text-on-highlight, Epiphany, Quod Libet,
debmirror, Nautilus, ...

  [for over 2 weeks]: @/net-connection-at-home-finally.md
  [with a lot of help]: http://mybroadband.co.za/vb/showthread.php/129619-Neotel-working-on-Linux!
