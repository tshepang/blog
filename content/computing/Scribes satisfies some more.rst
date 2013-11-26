Scribes satisfies some more
===========================

:date: 2008-11-26
:tags: Scribes



I'm currently running development version of Scribes (from bzr repo) and
it got fixes for two very annoying bugs:

-  On opening a non-UTF8 file you'd get a message asking you to open it
   via the app's file-selector, an uncomfortably long way around it; the
   version from bzr offers a choice of the encoding and then we live
   happily ever after.
-  A worse problem that occurred when opening the file described above
   is that on closing the error dialogue, all other open Scribes windows
   would also close.

All what this means is that Scribes remains installed on my machine(s).

--------------

**sidenote**: Code-folding is still absent although I won't need to use
it since `Geany`_ does a nice job already.

.. _Geany: http://tshepang.net/project-of-note-geany
