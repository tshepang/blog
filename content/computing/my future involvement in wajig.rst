my future involvement in wajig
==============================

:date: 2013-05-27
:tags: wajig, Python, Tracker



Some stuff I might work on in future:

- I want to start using argcomplete__ at some point, a more dynamic
  shell completion tool, replacing the current hand-rolled solution.
  I find shell programming hard, and argcomplete, which is inspired by
  optcomplete__ is a brilliant workaround.

- Someone asked me to restore gjig, the GUI tool that `I removed from
  wajig`__ some releases ago. This will be an opportunity to learn
  GTK+ again. I did a bit of it, even contributing patches (`Tracker
  project`__), but was never quite confident. It's very likely that I
  won't work on this... too much work.


--------------

Here's the work I did in the past working on wajig, have a look at
`its tag`_. Off the top of my head:

- improved, simplied packaging
- port to Python 3
- port to argparse (from getopt), which also meant proper handling of
  subcommands
- increased usage of python-apt, instead of hand-crafted (and ugly)
  code
- a few feature additions
- (lots of) modernising the code
- (lots of) cleaning up

And over 800 commits later, I am glad.


__ https://github.com/kislyuk/argcomplete
__ http://furius.ca/optcomplete/
__ http://tshepang.net/wajig-21-released
__ http://projects.gnome.org/tracker/
__ http://tshepang.net/tag/wajig/
