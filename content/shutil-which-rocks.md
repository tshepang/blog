+++
date = 2013-05-26
title = "shutil.which() rocks"
[taxonomies]
tags = ['Python', 'wajig']
+++

Unix/Linux systems have a simple (but useful) tool named which, whose
main purpose is to indicate where in the filesystem a particular
executable is installed. This functionality was added in Python 3.3, and
though simple, I was looking forward to its availability in Debian, just
so I could replace wajig's own equivalent functionality, which only
checked for file presence, and was hard-coded and therefore inflexible.
[shutil.which()], OTOH, looks for the given executable name in user's
PATH and is more thorough, since it also checks if the executable name
points to something that is actually executable. So, making use of this
new function resulted in code that is both more robust and [cleaner].

As a sidenote, this functionality [was first proposed in 2001]!

  [shutil.which()]: http://docs.python.org/3/library/shutil#shutil.which
  [cleaner]: https://github.com/gjwgit/wajig/commit/1b5b68fef401e097a97939e78555bb48e830dd1a
  [was first proposed in 2001]: http://bugs.python.org/issue444582
