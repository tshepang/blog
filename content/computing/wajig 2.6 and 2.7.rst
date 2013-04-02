wajig 2.6 and 2.7
=================

:date: 2012-07-02
:tags: wajig, Debian



Version 2.6 of wajig has changes so small that I did not bother writing
about its release, but was nevertheless very important because the
bash-completion now works a lot better than before, thanks to `Reuben
Thomas`_. I also changed wajig from accepting UUPERCASE subcommands,
since a few people on the mailing list expressed dislike, and that
includes project founder.

Version 2.7, the version that will be in the next stable release of
Debian [`update`_], Wheezy (Debian 7), fixes two bugs, one of which I
sort of intentionally broke in order to fix some issues with the
``--simulate`` and/or ``--teaching`` options. Someone `did complain
about this`_ which was good since it's a good indicator that someone
actually cared about the feature. That motivated me to fix it, and I
ensured that the fix was in before Debian freeze.

This project is my greatest contribution for this upcoming Debian
release, and although I stated that I do not intend to spend much time
on it in future in `a status report`_, it does not hurt much to fix a
bug here and there.

.. _Reuben Thomas: http://rrt.sc3d.org/
.. _update: http://tshepang.net/debian-7-will-release-with-wajig-273
.. _did complain about this: http://bugs.debian.org/670687
.. _a status report: http://tshepang.net/my-future-involvement-in-wajig
