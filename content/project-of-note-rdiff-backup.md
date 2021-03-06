+++
date = 2011-01-18
title = "project of note: rdiff-backup"
[taxonomies]
tags = ['project-of-note', 'GNOME']
+++

So I got my hands on a 250GB 2.5" portable HDD, which led to me to go
do proper backups again. I decided to go back to the familiar
[rdiff-backup] and I became exceedingly impressed by its thorough
documentation ([manpage], [FAQ], and the one place beginners should
start, [examples]), a myriad capabilities (over 60 command line
options), and an elegant design (the target directory looks exactly like
the original except for an extra directory named rdiff-backup-data,
which contains all that's needed to roll-back, restore, check stats,
...).

My usage:

    $ rdiff-backup --include-globbing-filelist rdiff-backup ~/ /media/backup

There, `~/conf/rdiff-backup` is a file that has a list of directories I
want to exclude in the backup, and `/media/backup` is the backup
destination.

---

There is a credible competitor in a form of duplicity, which is probably
superior since it's got encryption. This duplicity also got a bonus of
being used by some hot new GUI backup utility now [endorsed by Fedora]
and may in future be [an official part of GNOME], Déjà Dup.

  [rdiff-backup]: http://rdiff-backup.nongnu.org/
  [manpage]: http://rdiff-backup.nongnu.org/rdiff-backup.1.html
  [FAQ]: http://rdiff-backup.nongnu.org/FAQ.html
  [examples]: http://rdiff-backup.nongnu.org/examples.html
  [endorsed by Fedora]: http://lists.fedoraproject.org/pipermail/announce/2010-May/002815.html
  [an official part of GNOME]: http://mail.gnome.org/archives/desktop-devel-list/2010-February/msg00013.html
