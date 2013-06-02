using Python's subprocess module
================================

:date: 2011-01-26
:tags: Python



There are at least 2 ways to run a simple command like ``echo test`` in
Python: via the shell, or directly (via the kernel).

This is via the shell:

.. code-block:: python

    import subprocess
    subprocess.Popen("echo test", shell=True)

Output::

    test

This is via the kernel:

.. code-block:: python

    import subprocess
    p = subprocess.Popen(["echo", "test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    print(output)

Output::

    (b'testn', b'')

Not exactly what we want. The output is actually a tuple (**stdout**,
**stderr**). Note that by default, ``shell=False``, and that's why it's
not stated here.

To get the equivalent of what we get from the first example, we have to
do a bit more work:

.. code-block:: python

    import subprocess
    p = subprocess.Popen(["echo", "test"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    print(output[0].decode(), end="")

Output::

    test

The ``b`` thing indicates that the string is in bytes format. To get a
normal string from that, just run the string's `decode method`_. Also,
that I had to use the ``end`` argument on the `print function`_, was to
avoid an empty line on the terminal output.

As can be seen, this means we do much of the work ourself, but the
benefit is that we now have finer-grained control (e.g. we get to
control when to display the output). Another benefit is that it is more
secure to do it this way (I don't know the details, so see `shell
injection`_ for the argument).

further reading
---------------

-  There is a whole wealth of info on this from `a gentle tutorial`_
   where I learned this stuff. It also explains what pipes are
   (``subprocess.PIPE``)
-  Also, take a look at `the official doc for the Popen.communicate()
   method`_
-  `a great explanation`_ of what strings really are, and how they
   relate to Python 3


.. _decode method: http://docs.python.org/library/stdtypes.html?highlight=encode#str.decode
.. _print function: http://docs.python.org/library/functions.html#print
.. _shell injection: http://en.wikipedia.org/wiki/Shell_injection#Shell_injection
.. _a gentle tutorial: http://jimmyg.org/blog/2009/working-with-python-subprocess.html
.. _the official doc for the Popen.communicate() method: http://docs.python.org/library/subprocess.html#subprocess.Popen.communicate
.. _a great explanation: http://diveintopython3.net/strings.html
