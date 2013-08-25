packaging my first Qt app
=========================

:date: 2013-08-24
:tags: Debian, non-Python


Someone asked me to try get some KDE package into Debian. I estimated
that it would take me around 10 hours to get it into good enough shape
before asking some Debian Developer to upload it for me. Here goes
some rough estimates:

* **hour 1**: Find documentation on the subject; I got three after a
  quick search:

  - `Ubuntu Packaging Guide`__

  - `Create Ubuntu DEB package from a Qt application`__ (marked as
    deprecated, probably in favor of the official guide above)

  - Debian Packaging Tutorial (from Debian package,
    ``packaging-tutorial``)

* **hour 2-3**: Reading the Debian Packaging Tutorial which led me to
  reading ``dpkg-source`` manpage, using ``dh_make`` to create a
  ``debian/`` skeleton, and modifying the contents of that directory.

* **hour 4-6**: Struggling to kill the lintian complaint,
  ``binary-without-manpage``. I went as far as reading the source code
  (Perl) that performs the check, but that didn't help much. I could
  have saved hours by looking at the `Debian New Maintainers' Guide`__
  earlier. I also added ``export LDFLAGS=-Wl,-z,relro`` to
  ``debian/rules`` file to kill ``hardening-no-relro`` lintian
  warning.

* **hour 7-8**: Determine what dependencies would be needed by building from
  a clean chroot (pbuilder). This was with the help of Debian New
  Maintainers' Guide, again.

The resulting package now lives at
https://bitbucket.org/tshepang/ksig/src. The changes I made, the
actual packaging work, are in `this directory`__.


__ http://developer.ubuntu.com/packaging/html
__ https://wiki.ubuntu.com/PackagingGuideDeprecated/QtApplication
__ http://www.debian.org/doc/manuals/maint-guide
__ https://bitbucket.org/tshepang/ksig/src/ba388ea40c035340a5fccda1ced99e1bcfae94a3/debian
