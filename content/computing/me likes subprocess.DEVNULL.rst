me likes subprocess.DEVNULL
===========================

:date: 2013-04-11
:tags: Python, VCS


If you want to run an external process from within Python,
and are not interested in the error that process may emit,
there are a few ways,
and I will demonstrate by open a Python shell in a directory
that isn't version-controlled by Mercurial__:

#. So, we don't want to see this ugliness:

   >>> from subprocess import call
   >>> call('hg status'.split())
   abort: no repository found in '/home/tshepang/projects/pyramid' (.hg not found)!
   255

#. So, here's the simplest solution:

   >>> import os
   >>> from subprocess import call
   >>> call('hg status'.split(), stderr=open(os.devnull))
   255

   Problem: it leaves the file descriptor open... not good.


#. We fix:

   >>> import os
   >>> from subprocess import call
   >>> DEVNULL = open(os.devnull)
   >>> call('hg status'.split(), stderr=DEVNULL)
   255
   >>> DEVNULL.close()

   Much better, much uglier. (`example usage`__)

#. Something better:

   >>> import os
   >>> from subprocess import call
   >>> with open(os.devnull) as DEVNULL:
   ...     call('hg status'.split(), stderr=DEVNULL)
   255

   Looks much nicer, and is more convenient,
   unless we wanted to do something similar multiple times,
   in which case the previous example would be preferable.

#. Best solution:

   >>> import os
   >>> from subprocess import call, DEVNULL
   >>> call('hg status'.split(), stderr=DEVNULL)
   255

This `small and wonderful feature`__ is `new as of Python 3.3`__.


__ http://mercurial.selenic.com
__ https://bitbucket.org/tshepang/scripts/src/tip/vcs.py
__ http://hg.python.org/cpython/rev/eaf93e156dff
__ http://docs.python.org/3/whatsnew/3.3.html#subprocess
