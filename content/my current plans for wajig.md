+++
date = 2013-05-27
title = "my current plans for wajig"

[taxonomies]
tags = ['wajig', 'Python', 'Tracker']
+++

Some stuff I might work on in future:

-   I want to start using [argcomplete] at some point, a more dynamic
    shell completion tool, replacing the current hand-rolled solution. I
    find shell programming hard, and argcomplete, which is inspired by
    [optcomplete], is a brilliant workaround.
-   Someone asked me to restore gjig, the GUI tool that [I removed from
    wajig] some releases ago. This will be an opportunity to learn GTK+
    again. I did a bit of it, even contributing patches ([Tracker
    project]), but was never quite confident. It\'s very likely that I
    won\'t work on this\... too much work.

But ultimately, I would love for the standard Debian packaging tools to
get the point where they make wajig irrelevant. After all, wajig was
created to be a wrapper that helps ease the mess.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Here\'s the work I did in the past working on wajig, have a look at [its
tag]. Off the top of my head:

-   improved, simplified packaging
-   port to Python 3
-   port to argparse (from getopt), which also meant proper handling of
    subcommands
-   increased usage of python-apt, instead of hand-crafted (and ugly)
    code
-   a few feature additions
-   (lots of) modernising the code
-   (lots of) cleaning up

And over 800 commits later, I am glad.

  [argcomplete]: https://github.com/kislyuk/argcomplete
  [optcomplete]: http://furius.ca/optcomplete/
  [I removed from wajig]: http://tshepang.net/wajig-21-released
  [Tracker project]: http://projects.gnome.org/tracker/
  [its tag]: http://tshepang.net/tagss#wajig-ref
