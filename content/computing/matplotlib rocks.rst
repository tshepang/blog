matplotlib rocks
================

:date: 2012-07-19
:tags: Python


Have a look at this code:

.. sourcecode:: python

   from matplotlib import pyplot
   import random

   x_axis = range(10)
   pyplot.plot(x_axis, random.sample(range(10), 10))
   pyplot.plot(x_axis, random.sample(range(10), 10))
   pyplot.show()

With matplolib__ installed, running the code above should resulted in
the following image:

.. image:: images/matplotlib-1.png
   :alt: image resulting from running the code above

You will notice that there's 2 graphs drawn over the same axis, nothing
special. What I really loved about matplotlib is that I did not need to
specify what colors to use for any of the graphs (`as I did
previously`__). The colors were chosen automatically. It was helpful
especially in my case because I needed a way to specify an arbitrary
number of graphs. Without this magical feature, the code would be a lot
uglier.

Here goes:

.. sourcecode:: python

   from matplotlib import pyplot
   import argparse
   import random

   parser = argparse.ArgumentParser()
   parser.add_argument('number_of_graphs', type=int)
   args = parser.parse_args()

   x_axis = range(10)
   for n in range(args.number_of_graphs):
      pyplot.plot(x_axis, random.sample(range(10), 10), label=str(n))
   pyplot.legend()
   pyplot.show()

If I provide 3 as command line argument, I get this:

.. image:: images/matplotlib-2.png
   :alt: image resulting from running the code above

This feature left me pleasantly surprised.


__ http://matplotlib.org
__ http://tshepang.net/plotting-with-matplotlib
