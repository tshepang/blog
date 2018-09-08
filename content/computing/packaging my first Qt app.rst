---
date: '2013-08-27'
tags: 'Debian, non-Python'
title: packaging my first Qt app
---

Someone asked me to try get some KDE package into Debian. I estimated
that it would take me around 10 hours to get it into good enough shape
before asking some Debian Developer to upload it for me. Here goes some
rough estimates:

-   **hour 1**: Find documentation on the subject; I got a few after a
    quick search, which include the following:
    -   [Ubuntu Packaging Guide]
    -   Debian Packaging Tutorial (from Debian package,
        `packaging-tutorial`)
-   **hour 2-3**: Reading the Debian Packaging Tutorial which led me to
    reading `dpkg-source` manpage, using `dh_make` to create a `debian/`
    skeleton, and modifying the contents of that directory.
-   **hour 4-6**: Struggling to kill the lintian complaint,
    `binary-without-manpage`. I went as far as reading the source code
    (Perl) that performs the check, but that didn\'t help much. I could
    have saved hours by looking at the [Debian New Maintainers\' Guide]
    earlier. I also added `export LDFLAGS=-Wl,-z,relro` to
    `debian/rules` file to kill `hardening-no-relro` lintian warning.
-   **hour 7-8**: Determine what dependencies would be needed by
    building from a clean chroot (pbuilder). This was with the help of
    Debian New Maintainers\' Guide, again.
-   **hour 9-10**: Reading [Debian wiki page on Hardening] let me
    simplify my packaging further\... removing the need to specify
    hardening flags explicitly ([commit]). I also uploaded the package
    to <http://mentors.debian.net>, with the help of [DebianMentorsFaq].
    (**2014.03 update**: it has since been removed due to lack of
    activity)

The resulting package now lives at
<https://bitbucket.org/tshepang/ksig/src>. The changes I made, the
actual packaging work, are in [this directory].

  [Ubuntu Packaging Guide]: http://developer.ubuntu.com/packaging/html
  [Debian New Maintainers\' Guide]: http://www.debian.org/doc/manuals/maint-guide
  [Debian wiki page on Hardening]: https://wiki.debian.org/Hardening
  [commit]: https://bitbucket.org/tshepang/ksig/commits/f4c7b60157b79847f918e3d8b24a74e6c5bec929
  [DebianMentorsFaq]: https://wiki.debian.org/DebianMentorsFaq
  [this directory]: https://bitbucket.org/tshepang/ksig/src/f4c7b60157b79847f918e3d8b24a74e6c5bec929/debian
