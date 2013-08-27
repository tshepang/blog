packaging my first Qt app
=========================

:date: 2013-08-27
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

* **hour 9**: Reading `Debian wiki page on Hardening`__ let me
  simplify my packaging further... removing the need to specify
  hardening flags explicitly (commit__). I also read details of
  getting a package uploaded, with the help of DebianMentorsFaq__.

The resulting package now lives at
https://bitbucket.org/tshepang/ksig/src. The changes I made, the
actual packaging work, are in `this directory`__.


__ http://developer.ubuntu.com/packaging/html
__ https://wiki.ubuntu.com/PackagingGuideDeprecated/QtApplication
__ http://www.debian.org/doc/manuals/maint-guide
__ https://wiki.debian.org/Hardening
__ https://bitbucket.org/tshepang/ksig/commits/f4c7b60157b79847f918e3d8b24a74e6c5bec929
__ https://wiki.debian.org/DebianMentorsFaq
__ https://bitbucket.org/tshepang/ksig/src/f4c7b60157b79847f918e3d8b24a74e6c5bec929/debian
