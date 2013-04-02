project of note: M cross environment
====================================

:date: 2012-10-27
:tags: non-Debian, project-of-note



I spend several hours researching how to build a Qt app on Debian for
users who will run it on Windows. I also wanted it be just one binary at
the end so that deployment is just a matter of copying and running the
one executable. This means I needed to statically-compile the app, and
the sad news is that I first needed to build Qt itself statically.

If I had actually known of `M cross environment`_ (MXE), I would have
shaved nearly all of those 'wasted' hours. I am very grateful to the
developers, especially because building qt was just a matter of
installing `a few build dependencies`_ and running ``make qt``. An hour
or two later, I had newly cross-compiled Qt waiting for my use. It was
also pleasant that the app, in a form of a ``.exe`` file, just worked on
Windows 7.

Having a look around, the build system actually looks elegant, and is a
lot simpler than the scary mess that is `JHBuild`_.

.. _M cross environment: http://mxe.cc
.. _a few build dependencies: http://mxe.cc/#requirements-debian
.. _JHBuild: https://live.gnome.org/Jhbuild
