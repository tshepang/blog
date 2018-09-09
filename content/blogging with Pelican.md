+++
date = 2013-09-30
tags = ['blogging']
title = "blogging with Pelican"
+++

**notes**:

-   I have a separate post on [what I love about static website
    generators].
-   This post was first published on **2012-05-20**, which is before [I
    started using liquidluck], a competing tool.
-   And then I moved back **2013-09-29** due to development inactivity
    of liquidluck.

[Pelican] is a static blog generator; it converts marked-up text files
to html (Pelican supports [Markdown] and [reStructuredText]). The
resulting site is complete with an index (Archives view), Tags,
Categories, and Pages (for non-bloggy stuff like a CV or About Me file).

As for my blog, its tree structure looks like this ([repo]):

    build/...
    pages/about-me.rst
    posts/{arts/, computing/, misc/}
    CNAME
    fabfile.py
    new-post.py
    README.rst
    settings.py

-   The `build` directory is where the output of the build process is
    stored.
-   The `pages` directory is for any content that isn\'t blog posts.
-   The `posts` directory is where the large chunk of content lives, the
    blog posts themselves. Each of the four directories in there
    represent a Category, for example: if you place some file in
    `arts/`, the post will be marked as falling under **arts** Category.
-   I host my blog on GitHub, using a service the call GitHub Pages.
    `CNAME` is a file required by that service in the case where I want
    to use a domain other than `tshepang.github.io`. It\'s content is
    `tshepang.net`.
-   [fabfile.py] contains the build instructions, all for convenience so
    that I only need to run 2 commands, one for the build, and another
    for GitHub upload. However, I mostly just run one command that does
    both.
-   The [settings.py] file contains Pelican configuration. It should be
    somewhat mostly self-explanatory, but for those things that aren\'t
    so obvious, do consult the documentation.
-   [README.rst] has some basic instructions, as well as repository
    license.

Now as for the post itself, you need metadata to go with it. This is
stuff like title, date, and tags. It can be tedious to create all such
mundate stuff, especially the date. That\'s why I wrote [a script] that
generates that file and populates it with the given metadata:

    $ python new-post.py 'my blogging setup' misc --tags blogging

This is the metadata, and also the beginning of the file:

    my blogging setup
    =================

    :date: 2012-04-12
    :tags: blogging

The script also opens the file in my favorite editor, so I can start
adding content.

When I\'m done with the changes, I ensure I\'m in the root directory of
my blog, commit (`hg commit --message 'new post'`) and run:

    $ fab

That\'s a [fabric] command that uses the instructions found in
`fabfile.py`. It builds the site, and then pushes it to GitHub Pages. It
also pushes the sources to Bitbucket. Within a minute, the blog will be
updated.

  [what I love about static website generators]: http://tshepang.net/what-me-loves-about-static-website-generation
  [I started using liquidluck]: http://tshepang.net/from-pelican-to-liquidluck
  [Pelican]: http://pelican.notmyidea.org/
  [Markdown]: http://en.wikipedia.org/wiki/Markdown
  [reStructuredText]: http://en.wikipedia.org/wiki/ReStructuredText
  [repo]: https://bitbucket.org/tshepang/blog/src
  [fabfile.py]: https://bitbucket.org/tshepang/blog/src/tip/fabfile.py
  [settings.py]: https://bitbucket.org/tshepang/blog/src/tip/settings.py
  [README.rst]: https://bitbucket.org/tshepang/blog/src/tip/README.rst
  [a script]: https://bitbucket.org/tshepang/blog/src/tip/new-post.py
  [fabric]: http://fabfile.org
