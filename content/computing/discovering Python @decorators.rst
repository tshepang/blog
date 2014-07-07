discovering Python @decorators
==============================

:date: 2014-07-08
:tags: Python



There is a project at work where I needed to do the same action on
various functions. It's basically a checkpoint system where I'd write
some state to a file, but only when all the functionality in the given
functions executed successfully. It was a one-line change but I
thought it was a good excuse to create decorators for the first time
in my life.

Here is an example of a decorator function::

  def checkpoint(function):
      wrapper(*args, **kwargs):
          with open(PATH) as f:
              for line in f:
                  if function.__name__ in line:
                      return
          value = function(*args, **kwargs)
          with open(PATH, 'a+') as f:
              f.write(function.__name__)
          return value
      return wrapper

All it does is write some text to a file, and avoid running whatever
function will be *decorated* by it if there is a match in that
file. This would be an indicator that the function had already been
executed (in a previous run).

The following snippet sees the use of this decorator::

  @checkpoint
  def do_this(some_argument):
      # exit(1) on error
      ...

  @checkpoint
  def do_that(some_other_argument, some_optional_argument=None):
      # exit(1) on error
      ...

  if __name__ == '__main__':
      do_this('some value')
      do_that('some other value')


Without the decorator syntax, the same functionality would be achieved
with::

  def do_this(some_argument):
      # exit(1) on error
      ...
  do_this = checkpoint(do_this)

  def do_that(some_other_argument, some_optional_argument=None):
      # exit(1) on error
      ...
  do_that = checkpoint(do_that)

  if __name__ == '__main__':
      do_this('some value')
      do_that('some other value')

The latter format, though it presents less of a cognitive burden,
feels less of an obvious solution, and it's a bit uglier as
well. `PEP 380` is a detailed discussion written over 10 years ago
when the syntax was first added to the language.


__ http://legacy.python.org/dev/peps/pep-0318
