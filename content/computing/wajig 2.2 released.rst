wajig 2.2 released
==================

:date: 2011-05-09
:tags: Debian, wajig



Our friendly Debian developer agreed to upload yet another release of
wajig to Debian.

-  This one is quite special since it now uses Python 3.
-  It also does automatic dependency installation for DEB files. This
   part of the work took me longer because python-apt doesn't exactly
   make it easy. I even had to look in the code to be sure what exactly
   is happening. I ended up using a mixture of dpkg (for installation of
   stated DEBs, and to configure them) and python-apt (for the automatic
   installation part).
-  The WHICHPACKAGE command, which displays which packages the given
   file path belongs to, got improved. It was using custom
   implementation which was broken for some uses, but there are
   available tools (``dpkg --list`` for locally-installed packages and
   ``apt-file search`` for both local and remote packages) that do the
   job better, and I made use of them. These tools were probably not
   avaialable the time this feature was added to wajig.

