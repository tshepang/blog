packaging my first Qt app
=========================

:date: 2013-08-24
:tags: Debian, non-Python



* **hour 1**: Find documentation on the subject; I got three after a
  quick search:

  - `Ubuntu Packaging Guide`__

  - `Create Ubuntu DEB package from a Qt application`__ (marked as
    deprecated, probably in favor of the official guide above)

  - Debian Packaging Tutorial (from Debian package,
    ``packaging-tutorial``)

* **hour 2-3**: Reading the Debian Packaging Tutorial which led me to
  reading ``dpkg-source`` manpage, ``dh_make``, and modifying the
  resulting ``debian/`` directory contents.

* **hour 4-6**: Struggling to kill the lintian complaint,
  ``binary-without-manpage``. I went as far as reading the source code
  (Perl) that performs the check, but that didn't help much. I could
  have saved hours by looking at the `Debian New Maintainers' Guide`__
  earlier. Also added ``export LDFLAGS=-Wl,-z,relro`` to
  ``debian/rules`` file to kill ``hardening-no-relro`` lintian
  warning.

* **hour 7-8**: Determine what dependencies would be needed by building from
  a clean chroot (pbuilder). This was with the help of Debian New
  Maintainers' Guide, again.

The resulting package now lives at
https://bitbucket.org/tshepang/ksig/src.


__ http://developer.ubuntu.com/packaging/html
__ https://wiki.ubuntu.com/PackagingGuideDeprecated/QtApplication
__ http://www.debian.org/doc/manuals/maint-guide
