from Pelican to liquidluck
==========================

:date: 2013-03-20
:tags: blogging


**notes**:

- I have a separate post on `what I love about static website generators`_.
- This post was first published on **2012-07-05**,
  which is shortly after I started using `liquidluck`_.


why `Pelican`_ rocks
--------------------

-  has categories
   (`unlike nikola <https://github.com/ralsina/nikola/issues/163>`_)
-  post metadata:

   -  if Date is not specified, file mtime is used (unlike `blogofile`_)
   -  if Category is not specified, parent directory name is used
      (unlike blogofile)
   -  titles are allowed to have any character (unlike blogofile)
   -  there is an option to provide clean urls... remove trailing ``.html``
      (`unlike nikola <https://github.com/ralsina/nikola/issues/291>`__)

-  accepts ``.md`` extension for markdown files (unlike blogofile)
-  does not force one into having ugly date-based filesystem structure
   (`unlike tinkerer`_)

why Pelican rocks not
---------------------

- The default theme simply didn't fit my tastes, and `the 1 theme that
  I actually liked the most`_ gets 2nd-class treatment:

  + it hardly gets updates/maintenance, so lags behind
  + it's also a bit buggy, and I had to carry some patches (and submitted
    some)

  None of the other themes are satisfactory either,
  as you can see on the above-mentioned post.
  I spent way too long fiddling with them, and just couldn't be happy.

why liquidluck
--------------

So I have moved to `liquidluck`_ (aka Felix Felicis), and am hoping I
will not be 'forced' to move again. It's way too much work, and it took
multiple messages between me and the developer of this sleek new static
site generator just to get it to behave the way I like it.

I had to override stuff that's done by the software, by using `this script`_,
which helped give it the advantages that Pelican has over the
other generators I mentioned, while also solving the one problem Pelican
has.. lack a good-enough theme. This was achieved with the
help of that very helpful and responsive developer.

Note that `the post on how I used Pelican`_ still very much applies to
liquidluck. The differences can be found on bitbucket, where I host `the
sources`_.

issues
------

- There is no visible way, at least for the default theme, to subscribe
  to RSS feeds of individual Categories.
- The text is a bit blurry with the default theme, while the other
  theme that is available, named `Octopress`_, is just too ugly to use.
- Background color for `<code>` text is too unusual, and results in an
  ugly look. Does not fit the general general them, so should be grey really,
  which would match with that of `<pre>` text.


.. _Pelican: http://pelican.readthedocs.org/
.. _blogofile: http://blogofile.com/
.. _unlike tinkerer: https://bitbucket.org/vladris/tinkerer/issue/41
.. _the 1 theme that I actually liked the most: http://tshepang.net/favorite-pelican-themes
.. _liquidluck: http://liquidluck.readthedocs.org/
.. _this script: https://bitbucket.org/tshepang/blog/src/tip/custom.py
.. _the post on how I used Pelican: http://tshepang.net/blogging-with-pelican
.. _the sources: https://bitbucket.org/tshepang/blog/src
.. _Octopress: https://github.com/lepture/liquidluck-theme-octopress
.. _what I love about static website generators: http://tshepang.net/what-me-loves-about-static-website-generation
