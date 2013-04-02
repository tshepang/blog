blogging with Pelican
=====================

:date: 2013-03-18
:tags: blogging


**notes**:

- I have a separate post on `what I love about static website generators`_.
- This post was first published on **2012-05-20**,
  which is before `I started using liquidluck`_, a competing tool.


`Pelican`_ is a static blog generator. What it does is build files (with
`Markdown`_ or `reStructuredText`_ markup) from some specific directory,
and spits out html into another directory. The resulting site is
complete with an index (Archives view), tags, categories, and pages. The
next step is to upload the site to some host, which in my case is
`GitHub Pages`_.

As for my blog, its tree structure looks like this::

    build/...
    pages/{about-me.md, key-posts.md}
    posts/{arts/, computing/, misc/, movies/}
    CNAME
    fabfile.py
    new-post.py
    settings.py

-  The ``build`` directory is where the output of the build process is
   stored.

-  The ``pages`` directory is where lives key content that does not need
   dating, e.g. and About Me page

-  The ``posts`` directory is where the large chunk of content live, the
   blog posts themselves. Each of the four directories in there
   represent a Category, for example: if you place some file in
   ``arts/``, the post will be marked as falling under **arts**
   Category.

-  ``CNAME`` is a file required by GitHub pages in the case where I want
   to use a domain other than ``tshepang.github.com``. What I have in
   that text file is ``tshepang.net``.

-  `fabfile.py`_ contains the build instructions, all for convenience
   so that I only need to run 2 commands, one for the build, and another
   for GitHub upload. However, I mostly just run one command that does
   both.

-  The `settings.py`_ file contains Pelican configuration.

It should be somewhat mostly self-explanatory, but for those things that
aren't so obvious:

-  ``ARTICLE_URL = '{slug}'`` allows pages to be visited without the
   ``.html`` extension. The same applies to ``CATEGORY_URL`` and ``PAGE_URL``
-  ``REVERSE_ARCHIVE_ORDER`` is so that the newest posts be shown first
   in Archive view; to me this setting `shouldn't be needed`_ since it's
   common practice to do this. I don't even remember any one blog
   showing oldest posts first, in whatever view.
   ``REVERSE_CATEGORY_ORDER`` should also do the same, but `it's broken
   at the moment`_.
-  ``THEME`` is where you specify `a choice of theme`_ to use. Luckily
   there's a bunch to choose from, even though `I liked only a few`_.
-  ``TYPOGRIFY`` is `supposed to make text look better`_, But don't ask
   me cuz I can't really tell.

Now as for the post itself, you need metadata to go with it. This is
stuff like title, date, and tags. It can be tedious to create all such
mundate stuff, especially the date. That's why I wrote `a script`_ that
generates that file and populates it with that metadata::

    $ python new-post.py 'my blogging setup' misc --tags blogging

This is the metadata, and also the beginning of the file::

    my blogging setup
    =================

    :date: 2012-04-12
    :tags: blogging

The script also opens the file in my favorite editor, so I can start
adding content.

When I'm done and happy with my latest changes,
I ensure I'm in the root directory of my blog, commit
(``hg commit --message 'new post'``) and run::

    $ fab

That's a `fabric`_ command the uses the instructions found in
``fabfile.py``. It builds the site, and then pushes is to GitHub pages.
It also pushes the sources to BitBucket. Within a minute, the blog will
be updated.


.. _I started using liquidluck: http://tshepang.net/from-pelican-to-liquidluck
.. _Pelican: http://pelican.notmyidea.org/
.. _Markdown: http://en.wikipedia.org/wiki/Markdown
.. _reStructuredText: http://en.wikipedia.org/wiki/ReStructuredText
.. _GitHub Pages: http://pages.github.com/
.. _shouldn't be needed: https://github.com/getpelican/pelican/issues/304
.. _it's broken at the moment: https://github.com/getpelican/pelican/issues/308
.. _a choice of theme: https://github.com/getpelican/pelican-themes
.. _I liked only a few: http://tshepang.net/favorite-pelican-themes
.. _supposed to make text look better: http://static.mintchaos.com/projects/typogrify/
.. _publicly visible in Bitbucket: https://bitbucket.org/tshepang/blog
.. _fabric: http://fabfile.org
.. _fabfile.py: https://bitbucket.org/tshepang/blog-pelican/src/tip/fabfile.py
.. _settings.py: https://bitbucket.org/tshepang/blog-pelican/src/tip/settings.py
.. _a script: https://bitbucket.org/tshepang/blog-pelican/src/tip/new-post.py
.. _what I love about static website generators: http://tshepang.net/what-me-loves-about-static-website-generation 
