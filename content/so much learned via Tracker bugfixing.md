+++
date = 2010-04-02
tags = ['GNOME', 'Tracker']
title = "so much learned via Tracker bugfixing"
+++

It\'s been maybe over a year since I\'ve submitted a patch to any FLOSS
project and have done so [three][] [times][] [today], all for [Tracker],
perhaps my most favorite of all pieces of code.

This started with me nagging [Martyn Russell], Release Manager for
Tracker, about the suckage which was exposed by my usage of Tracker\'s
preferences GUI. He proceeded to encourage me to write a patch, which I
did. Later on [Michael Natterer] of GIMP fame guided me on some UI
polish work.

I consumed much info (and time) during the process, which entailed
looking at the following:

-   [GTK+ API]
-   Tracker\'s configuration internals.
-   1st look at [Vala], the language with which the preferences GUI is
    written.
-   Tinkering with [Glade], a RAD tool for quick GUI development, which
    makes things so much easier, especially considering that GTK+ isn\'t
    so straightforward.

  [three]: https://bugzilla.gnome.org/show_bug.cgi?id=614608
  [times]: https://bugzilla.gnome.org/show_bug.cgi?id=614609
  [today]: https://bugzilla.gnome.org/show_bug.cgi?id=614610
  [Tracker]: http://projects.gnome.org/tracker/
  [Martyn Russell]: http://blogs.gnome.org/mr/
  [Michael Natterer]: http://gimpfoo.de/
  [GTK+ API]: http://developer.gnome.org/gtk2/stable/
  [Vala]: http://live.gnome.org/Vala
  [Glade]: http://glade.gnome.org/
