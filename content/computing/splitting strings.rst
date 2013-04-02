splitting strings
=================

:date: 2011-02-01
:tags: Python, non-Python



If I have a string with spaces, and wanted to split it into a
list/array, I would use this:

.. code-block:: python

    split_string = "a b c".split()
    print(split_string)

Output::

    ['a', 'b', 'c']

I can go ahead and specify a delimiter (which character the string must
split on):

.. code-block:: python

    split_string = "string with spaces".split(" ")
    print(split_string)

I get the same result::

    ['a', 'b', 'c']

But what if my string wasn't so forgiving?

.. code-block:: python

    split_string = "a b  c".split(" ")
    print(split_string)

Output::

    ['a', 'b', '', 'c']

Not exactly what we want. Leaving the delimiter out gives us the exact
same list as when we had this with a forgiving string.

Anyways, the point is that for a lot of cases, probably a majority, when
one wants to perform a string split, it's because they want to delimit
it with spaces. So, Python covers for that common use-case. That's a bit
of `magic`_ (`justification`_) one might take for granted, because it's
not available in PHP and Java. I'm here only going to show Java
examples. PHP examples aren't that much different though.

Here goes:

.. code-block:: java

    import java.util.Arrays;
    String[] splitString = "a b  c".split(" ");
    System.out.println(Arrays.asList(splitString));

Output::

    [a, b, , c]

That's not what we want, so in order to cover for my unforgiving string,
I get to use regular expressions (regexp)?

.. code-block:: java

    import java.util.Arrays;
    String[] splitString = "string with spaces".split(" +");
    System.out.println(Arrays.asList(splitString));

Output::

    [a, b, c]

The ``+`` in the ``split()`` method indicates that the match can either
be one or more consecutive spaces.

That's not what we want, so in order to cover for my unforgiving string,
I get to use regular expressions (regexp)?

.. code-block:: java

    String[] splitString = "string with spaces".split(" +");
    System.out.println(Arrays.asList(splitString));

Output::

    [a, b, c]

But what if the string was even less forgiving. In this case, having
tabs as well? We need some more regexp help:

.. code-block:: java

    import java.util.Arrays;
    String[] splitString = "a    bnc".split("\s+");
    System.out.println(Arrays.asList(splitString));

Output::

    [a, b, c]

The ``s`` matches any white space.

With Python, I expected the default way to work but it didn't, but came
back disappointed:

.. code-block:: python

    split_string = "a    bnc".split(" ")
    print(split_string)

Output::

    ['at', 'bnc']

Perhaps it's a philosophical difference, but it's harder to do this with
Python. This is the only thing so that I found easier to achieve in Java
than in Python:

.. code-block:: python

    import re
    split_string = re.split("s+", "a    bnc")
    print(split_string)

...and we finally get what we want::

    ['a', 'b', 'c']


.. _magic: http://docs.python.org/library/stdtypes.html#str.split
.. _justification: http://bugs.python.org/issue1367936
