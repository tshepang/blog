plotting with matplotlib
========================

:date: 2011-02-17
:tags: Python



Here's drawing a simple graph:

.. code-block:: python

    from matplotlib import pyplot
    x = range(10)  # a list of 10 integers, 0-9
    y = range(10)
    pyplot.plot(x, y)
    pyplot.show()

And now for something a little more interesting:

.. code-block:: python

    import random
    from matplotlib import pyplot
    x = range(10)
    y = random.sample(range(10), 10)
    pyplot.plot(x, y)
    pyplot.show()

We can have more than one graph on a single figure:

.. code-block:: python

    import random
    from matplotlib import pyplot
    x = range(10)
    y1 = random.sample(range(10), 10)
    y2 = random.sample(range(10), 10)
    pyplot.plot(x, y1, x, y2)
    pyplot.show()

What if the two graphs have much differing ranges:

.. code-block:: python

    import random
    from matplotlib import pyplot
    x = range(10)
    y1 = random.sample(range(10), 10)
    y2 = random.sample(range(100, 110), 10)
    pyplot.plot(x, y1, x, y2)
    pyplot.show()

Depending on need, that might not be ideal.
So let's create two separate y-axes:

.. code-block:: python

    import random
    from matplotlib import pyplot
    x = range(10)
    y1 = random.sample(range(10), 10)
    y2 = random.sample(range(100, 110), 10)
    pyplot.plot(x, y1)
    pyplot.twinx()
    pyplot.plot(x, y2)
    pyplot.show()

Yeah, not exactly ideal. We lost the automatic coloring, and we don't
even know which graph is which. Let's do better:

.. code-block:: python

    import random
    from matplotlib import pyplot
    x = range(10)
    y1 = random.sample(range(10), 10)
    y2 = random.sample(range(100, 110), 10)
    pyplot.plot(x, y1, "red")
    pyplot.ylabel("y1", color="red")
    pyplot.twinx()
    pyplot.plot(x, y2, "blue")
    pyplot.ylabel("y2", color="blue")
    pyplot.show()

This was done with the help of `this example`_. There's a heck of a
`lot`_ `more`_.

further reading
---------------

-  built-in function: `range`_
-  module: `random`_
-  3rd-party module: `matplotlib.pyplot`_
-  `matplotlib documentation`_

.. _this example: http://matplotlib.sourceforge.net/examples/api/two_scales.html
.. _lot: http://matplotlib.sourceforge.net/examples/index.html
.. _more: http://matplotlib.sourceforge.net/gallery.html
.. _range: http://docs.python.org/library/functions#range
.. _random: http://docs.python.org/library/random
.. _matplotlib.pyplot: http://matplotlib.sourceforge.net/api/pyplot_api.html
.. _matplotlib documentation: http://matplotlib.sourceforge.net/contents.html
