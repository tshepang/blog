project of note: Iotop
======================

:date: 2011-02-25
:tags: project-of-note



`Iotop`_ displays disk I/O usage of individual process, in a way similar
to top. What I really loved though is that it allows one to display the
accumulated amount of I/O on any of the DISK READ, DISK WRITE, SWAPIN,
and IO (overall). This is through a nifty interface:

-  You just press ``a`` on the keyboard, and it will sort the hungriest
   processes on top.
-  Reversing the order, you just press ``r``.
-  If you want to sort by other colums, you just press the left/right
   key.

`The presentation`_ is rather busy, and it doesn't have the myriad
options that ``top`` has (e.g. I can't chose to hide any of the columns
I'm uninterested in), but it's more than good enough for it's specific
purpose.

.. _Iotop: http://guichaz.free.fr/iotop/
.. _The presentation: http://guichaz.free.fr/iotop/iotop_big.png
