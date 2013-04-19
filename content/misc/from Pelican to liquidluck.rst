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

- It has categories
  (`unlike nikola <https://github.com/ralsina/nikola/issues/163>`_)

- Post metadata:

  -  if Date is not specified, file mtime is used (unlike `blogofile`_)
  -  if Category is not specified, parent directory name is used
     (unlike blogofile)
  -  titles are allowed to have any character (unlike blogofile)
  -  there is an option to provide clean urls... remove trailing ``.html``
     (`unlike nikola <https://github.com/ralsina/nikola/issues/291>`__)

- Does not force one into having ugly date-based filesystem structure
  (`unlike tinkerer`_)


why Pelican rocks not
---------------------

The default theme simply didn't fit my tastes,
and `the other themes weren't so satisfactory`_.
I spent way too long fiddling with them, and just couldn't be happy.


why liquidluck
--------------

So I have moved to `liquidluck`_,
and am hoping I will not be 'forced' to move again.
It's way too much work, and it took multiple messages between me and
`the developer`_ of this sleek new static site generator just to get it
to behave the way I like it.

I had to override stuff that's done by the software, by using `this script`_,
which helped give it the advantages that Pelican has over the
other generators I mentioned, while also solving the one problem Pelican
has.. lack of a good-enough theme.
This was achieved with the help of that very helpful and responsive developer.

issues
------

- There is no visible way, at least for the default theme, to subscribe
  to RSS feeds of individual Categories.
- The text is a bit blurry/faint with the default theme,
  and none of `the other ones`_ are close to good-enough for my liking.
- Background color for ``<code>`` text is too unusual,
  and results in an ugly look.
  It does not fit with the general general theme, so should be grey really,
  which would match with that of ``<pre>`` text.


.. _Pelican: http://pelican.readthedocs.org
.. _blogofile: http://blogofile.com
.. _unlike tinkerer: https://bitbucket.org/vladris/tinkerer/issue/41
.. _the other themes weren't so satisfactory: http://tshepang.net/favorite-pelican-themes
.. _liquidluck: http://liquidluck.readthedocs.org
.. _this script: https://bitbucket.org/tshepang/blog/src/tip/custom.py
.. _what I love about static website generators: http://tshepang.net/what-me-loves-about-static-website-generation
.. _the other ones: http://tshepang.net/looking-at-liquidluck-themes
.. _the developer: http://lepture.com
