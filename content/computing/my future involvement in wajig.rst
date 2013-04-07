my future involvement in wajig
==============================

:date: 2012-04-11
:tags: wajig, Python, Tracker



After releasing `version 2.5`_, I don't intend spending much more time
in wajig. I want to learn `CPython`_ code in earnest, you know fixing
bugs, improving documentation, increasing test coverage. I've already
started with that, and some of my work has been committed, but am not
satisfied yet. There's still a few bugs I want to work, blog posts to
read, videos to watch... I suspect doing this is one good way towards
being a decent developer.

This doesn't mean I will abandon wajig of course. It means I intend to
keep it on maintenance mode (i.e. fixing bugs). I will even work on an
odd feature request (there aren't many of those). But one thing I might
work on:

-  someone asked me to restore gjig, the GUI tool that I removed from
   wajig some releases ago; this will be an opportunity to learn GTK+
   again; I did a bit of it, even contributing patches (`Tracker
   project`_), but was never quite confident
-  whenever someone ports `optcomplete`_ to `argparse`_, I gonna put it
   in wajig; I find shell programming hard, and optcomplete is a
   brilliant workaround

--------------

For the work I did in the past working on wajig, have a look at `its
tag`_. Off the top of my head:

-  improved, simplied packaging
-  port to Python 3
-  port to argparse (from getopt), which also meant proper handling of
   subcommands
-  increased usage of python-apt, instead of hand-crafted (and ugly)
   code
-  a few feature additions
-  (lots of) modernising the code
-  (lots of) cleaning up

And over 700 commits later, I am glad.

.. _version 2.5: http://tshepang.net/wajig-25-released
.. _CPython: http://doc.python.org/devguide
.. _Tracker project: http://projects.gnome.org/tracker/
.. _optcomplete: http://furius.ca/optcomplete/
.. _argparse: http://docs.python.org/dev/library/argparse
.. _its tag: http://tshepang.net/tag/wajig/
