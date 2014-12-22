Python wishes
=============

:tags: Python


None of these is likely to happen at all.
It's even safe to use the word *never* with a great amount of certainty;
but I wanted to document them anyway, if for no other reason than rescue
them from the exclusiveness of my mind:

* add a ``prepend`` method to list objects, make it as efficient as
  ``collections.deque``, then remove the latter

* remove ``f.readlines()``;
  ``list(f)`` is a clearer and more general replacement (source__).

* rm ``os.system``, ``os.popen*`` and relatives;
  we already have the `subprocess module`__

* rid of all forms of string formatting,
  other than `Advanced String Formatting`__;
  do it everywhere, including the `logging module`__

* change module names to be PEP-compliant, everywhere

* remove ``lambda``; it's not Pythonic, and just feels like a wart;
  it also does a good job of making Python code less readable

* make ``item`` go out of scope when outside for-loops like ``for item
  in range(count)``


__ http://bugs.python.org/issue13510#msg186940
__ http://docs.python.org/3/library/subprocess
__ http://docs.python.org/3/library/string#string-formatting
__ http://docs.python.org/3/library/logging
