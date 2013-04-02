Scribes; building GNOME 2.16 with Debian
========================================

:date: 2007-04-17
:tags: Debian, GNOME



In order to minimize bandwidth usage, I have recently restricted myself
to building a local repository consisting only of source packages as
opposed to the previous times when I only did binary package downloads.
This was helped by my recently-acquired skill of building Debian
packages from source, most often just 3 simple commands:

1. ``apt-get build-dep nautilus`` (retrieves nautilus' build
   dependencies)
2. ``sudo apt-get source --build nautilus`` (downloads nautilus' source
   into current directory and builds a Debian binary package out of it)
3. ``sudo dpkg --install *deb`` (installs the .deb files stated on the
   command line onto the system)

I've been practicing the above procedure on several packages, including
monsters like Linux, GLibC and OpenOffice.org, and it worked pretty
well.

I did the same for GNOME 2.16/2.18 packages (Debian GNOME maintainers
haven't completed the job of migrating to 2.18 yet) available in
Debian's `Experimental repository`_. This effort was initially targetted
at building 2.16 version of python-gnome and 2.10 version of python-gtk2
in order to try to build Scribes, after a previous failure. But then,
since I had much GNOME infrastructure (libgtk2, libbonono, libgnomevfs2,
...) already built, I proceeded on building some of my favorites as well
(nautilus, gnome-terminal, gedit, etc.), and, even though I only had ~3
hours of sleep, I woke up a happy being.

I almost forgot to mention that Scribes managed to run properly, though
I didn't have enough time to check it out properly. It sure looks good
and am looking forward to it.

**[a day later]**

Although I managed to get `Scribes`_ to hang at least once, here's the
more positive facts:

-  I really do love the auto-save feature
-  the interface is real clean, providing a fresh departure from the
   stately (and beloved) `gedit`_
-  it's got word-suggestion by default
-  there's some other nifty nice features like various editing
   capabilities which are far more powerful than gedit provides

.. _Experimental repository: http://packages.debian.org/experimental/
.. _Scribes: http://scribes.sourceforge.net/index.html
.. _gedit: http://www.gnome.org/projects/gedit/
