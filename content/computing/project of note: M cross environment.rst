project of note: M cross environment
====================================

:date: 2013-04-20
:tags: non-Debian, project-of-note, non-Python


I spend several hours researching how to build a Qt app (written in C++)
on Debian for users who will run it on Windows.
I also wanted it be just one binary at the end so that deployment is just
a matter of copying and running the one executable.
This means I needed to statically-link the app,
and the sad news is that I first needed a statically-linked Qt.

If I had actually known of `M cross environment`_ (MXE), I would have
shaved nearly all of those 'wasted' hours. I am very grateful to the
developers, especially because building Qt was mainly a matter of
installing `a few build dependencies`_ and running ``make qt``. An hour
or two later, I had a newly cross-compiled Qt waiting for my use. It was
also pleasant that the app, in a form of a ``.exe`` file, just worked on
Windows 7.

Having a look around, the build system actually looks elegant, and is a
lot simpler than the scary mess that is `JHBuild`_.

----

I have published two guides on Stack Overflow on how this works,
`one for Qt 4`__ and `another for Qt 5`__.


__ http://stackoverflow.com/a/13211922/321731
__ http://stackoverflow.com/a/14170591/321731
.. _M cross environment: http://mxe.cc
.. _a few build dependencies: http://mxe.cc/#requirements-debian
.. _JHBuild: https://live.gnome.org/Jhbuild
