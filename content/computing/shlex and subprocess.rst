shlex and subprocess
====================

:date: 2011-01-25
:tags: Python



I learned about a module called `shlex`_. It's stated to be a simple
lexical analyzer, and I don't really know what this means, but I found
at least one of its uses. It provides a convenience method that lets me
split a command line string, to feed into `subprocess`_ module.

Let's say I want to run the command ``/bin/cat 'file with spaces'`` from
within ``python``. A normal ``split`` won't work, because it uses white
space as a delimiter (by default). To test, I will create a file named
"**file with spaces**" and add text
(``content of 'file with spaces'``).

.. code-block:: sh

    $ echo 'content of file with spaces' > 'file with spaces'

And here's the code, using the normal split method:

.. code-block:: python

    import subprocess
    cmd = "/bin/cat 'file with spaces'"
    formatted_cmd = cmd.split()
    subprocess.Popen(formatted_cmd)

Output:

.. code-block:: sh

    /bin/cat: 'file: No such file or directory
    /bin/cat: with: No such file or directory
    /bin/cat: spaces': No such file or directory

That's when ``shlex`` module gets to be useful.

.. code-block:: python

    import shlex, subprocess
    cmd = "/bin/cat 'file with spaces'"
    formatted_cmd = shlex.split(cmd)
    subprocess.Popen(formatted_cmd)

Output::

    content of 'file with spaces'


.. _shlex: http://docs.python.org/library/shlex.html
.. _subprocess: http://docs.python.org/library/subprocess.html
