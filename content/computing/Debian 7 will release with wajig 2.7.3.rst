Debian 7 will release with wajig 2.7.3
======================================

:date: 2012-07-17
:tags: wajig, Debian



I once claimed that Debian 7 "wheezy" will release with version 2.7 of
wajig, but soon after, I noticed that an exception occurs if you run a
command like ``wajig new`` if one of the newly-available packages was
available for the configured foreign architecture, but not for the
native one (`bug 679969`_). To fix that, I released 2.7.1, but I
submitted a dirty tarball for upload, so had to resubmit, ending up
releasing 2.7.2. Later on, someone noticed that `a certain subcommand
wasn't recognized`_, and I released 2.7.3 which fixes the issue.

.. _bug 679969: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=679969
.. _a certain subcommand wasn't recognized: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=681309
