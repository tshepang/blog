thanks to the Debian backports team
===================================

:date: 2011-07-14
:tags: Debian



So I got this new HP laptop, Probook 4530s, and installed Debian 6
(Squeeze) on it. I was left sitting with two unbearable problems:

-  The touchpad wasn't fully operational (GNOME Mouse Preferences didn't
   have a Touchpad tab where I could do the settings).
-  The video driver seemed to have a problem according to the output of
   **xvinfo** (``no adaptors present``).

I curiously looked at `the backports`_, and found Linux kernel 2.6.38
(Squeeze has 2.6.32). I didn't expect much from it, but installed it
anyway since I know that it has improved desktop responsiveness. I was
pleasantly surprised to find that it fixed the above two problems.
Loveliness.

On another note, I found that **``mercurial``** 1.8 also has a backport.
This is great news because I have repositories I created with that
version and the format is incompatible with Squeeze's 1.6.

.. _the backports: http://backports.debian.org/
