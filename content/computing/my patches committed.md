---
date: '2010-04-06'
tags: 'GNOME, Tracker'
title: my patches committed
---

So, two of the [patches I created] for [Tracker] have been committed
(commit [1][patches I created], [2])!

I consumed much info (and time) during the process, which entailed
looking at Git usage (branch, checkout, commit, format-patch, \...)
through [Philip van Hoof]\'s guidance.

------------------------------------------------------------------------

Philip van Hoof also [fixed] a hard-to-reproduce bug which was a pain
for me. The fix is a workaround for a [GTK+] bug.

  [patches I created]: http://tshepang.net/so-much-learned-via-tracker-bugfixing
  [Tracker]: http://projects.gnome.org/tracker/
  [2]: http://git.gnome.org/browse/tracker/commit/?id=ade2655a2f9fecf7100d58a8908493b9d71e2273
  [Philip van Hoof]: http://pvanhoof.be/blog/
  [fixed]: http://git.gnome.org/browse/tracker/commit/?id=c5a15f8231c63488605d799b9670aba01898fde4
  [GTK+]: http://www.gtk.org/
