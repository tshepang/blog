+++
date = 2018-09-14
title = "1st FLOSS patch contribution"

[taxonomies]
tags = ['GNOME', 'Tracker']
+++

Back in 2007,
I sent a patch that slightly improved the README of [Tracker],
a project that is meant to be a data indexer (like [Google  Desktop]) and much more.
It is the first ever FLOSS contribution I ever made:


```diff
--- /home/wena/FLOSS/src/tracker-0.5.3/ChangeLog
+++ /home/wena/FLOSS/src/tracker-0.5.3-note-on-threadsafety/ChangeLog
@@ -1,3 +1,6 @@
+2007-01-03  Tshepang Lekhonkhobe <tshepang@gmail.com>
+
+	* Added a note on the reason why SQLite is statically-linked

 2006-12-23  Jamie McCracken <jamiemcc at gnome org>

--- /home/wena/FLOSS/src/tracker-0.5.3/README
+++ /home/wena/FLOSS/src/tracker-0.5.3-note-on-threadsafety/README
@@ -90,7 +90,7 @@

 Run time dependencies (also needed for build) :

-Sqlite 3.2+
+Sqlite 3.2+ (this is statically-linked due to the lack of guarantee of threadsafety in distro versions)
 libdbus (0.50 +)
 dbus-glib bndings (0.50 +)
 glib (2.6+)
```

That year,
I went on to make some more minor code patches,
learning a few things along the way,
like [GTK+] and [GLib] APIs.


  [Tracker]: http://projects.gnome.org/tracker/
  [Google Desktop]: http://en.wikipedia.org/wiki/Google_Desktop
  [GTK+]: http://developer.gnome.org/gtk2/stable/
  [GLib]: http://developer.gnome.org/glib/stable/
