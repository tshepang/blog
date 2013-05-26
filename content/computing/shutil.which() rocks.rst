shutil.which() rocks
====================

:date: 2013-05-26
:tags: Python, wajig



Unix/Linux systems have a simple (but useful) tool named `which`,
whose main purpose is to indicate where in the filesystem a particular
executable is installed. This functionality was added in Python 3.3,
and though simple, I was looking forward to its availability in
Debian, just so I could replace wajig's own equivalent functionality,
which only checked for file presence, and was hard-coded and therefore
inflexible. shutil.which()__, OTOH, looks for the given executable name
in user's PATH and is more thorough, since it also checks if the
executable name points to something that is actually executable.  So,
making use of this new function resulted in more robust code, as well
as `a lot cleaner`__.

As a sidenote, this functionality `was first proposed in 2001`__!


__ http://docs.python.org/3/library/shutil#shutil.which
__ https://code.google.com/p/wajig/source/detail?r=e419e439e47f880ab17f6394e3faaa8ce3b15fe1
__ http://bugs.python.org/issue444582
