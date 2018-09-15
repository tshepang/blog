+++
date = 2012-03-29
title = "wajig 2.4 released"

[taxonomies]
tags = ['Debian', 'wajig']
+++

Less than a week after releasing 2.3, someone discovered a bug when
running the NEW subcommand. All wajig did was fall flat with an ugly
exception, making this some sort of emergency release. Anyways, I
already had some nice improvements, so I released those as well:

-   The INSTALL subcommand can now be given a mixture of filenames, .deb
    files, and normal package names, and will be able to install the
    packages specified. Previously, only one of these 3 types could be
    installed at a time.
-   Apparently the reasons I gave for removing the +++simulate and
    +++teaching (now renamed to +++teach) options in 2.3 weren't good
    enough, so I reinstated them.
-   The bash completer now completes both lower-case and upper-case
    subcommands, thanks to [Reuben Thomas], an avid wajig user.
-   There's a few other changes, so [here's the gory details].

  [Reuben Thomas]: http://rrt.sc3d.org/
  [here's the gory details]: http://packages.qa.debian.org/w/wajig/news/20120327T130420Z.html
