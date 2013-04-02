so much learned via Tracker bugfixing
=====================================

:date: 2010-04-02
:tags: GNOME, Tracker



It's been maybe over a year since I've submitted a patch to any FLOSS
project and have done so `three`_ `times`_ `today`_, all for `Tracker`_,
perhaps my most favorite of all pieces of code.

This started with me nagging `Martyn Russell`_, Release Manager for
Tracker, about the suckage which was exposed by my usage of `Tracker's
preferences GUI`_. He proceeded to encourage me to write a patch, which
I did. Later on `Michael Natterer`_ of GIMP fame guided me on some UI
polish work.

I consumed much info (and time) during the process, which entailed
looking at the following:

-  `GTK+ API`_
-  Tracker's configuration internals.
-  1st look at `Vala`_, the language with which the preferences GUI is
   written.
-  Tinkering with `Glade`_, a RAD tool for quick GUI development, which
   makes things so much easier, especially considering that GTK+ isn't
   so straightforward.

.. _three: https://bugzilla.gnome.org/show_bug.cgi?id=614608
.. _times: https://bugzilla.gnome.org/show_bug.cgi?id=614609
.. _today: https://bugzilla.gnome.org/show_bug.cgi?id=614610
.. _Tracker: http://projects.gnome.org/tracker/
.. _Martyn Russell: http://blogs.gnome.org/mr/
.. _Tracker's preferences GUI: http://projects.gnome.org/tracker/images/screenshots/screenshot-tracker-preferences.png
.. _Michael Natterer: http://gimpfoo.de/
.. _GTK+ API: http://developer.gnome.org/gtk2/stable/
.. _Vala: http://live.gnome.org/Vala
.. _Glade: http://glade.gnome.org/
