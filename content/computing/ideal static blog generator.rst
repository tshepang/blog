ideal static blog generator
===========================

:date: 2013-05-12
:tags: blogging


Anything not listed below is either stuff I take for granted or simply
missed:

* reStructuredText__ support is mandatory, and so is being written in
  Python (I is a fanboy).

* Landing page should not display blog content; an exception is if
  this is limited to the latest post (which `Just Read`__ theme of
  Pelican__ does nicely).

* Categories should be determined by directory into which a post is
  placed if not explicitly specified (in file metadata section).

* Ability to determine post date from file mtime.

* Post Date should always precede post content.

* An option to have clean urls (i.e. trailing ``.html`` removed).

* Date-based directory structure should not be mandatory, `which is
  the case with Tinkerer`__.

* Inline literals and literal blocks (for code) should be
  distinguished by background colour; using different fonts is not
  good enough.

* Tags should be displayed on each post.

  - bonus: Categories too

* A visible Atom/RSS feed icon please.


__ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
__ https://github.com/getpelican/pelican-themes/tree/master/Just-Read
__ http://blog.getpelican.com/
__ https://bitbucket.org/vladris/tinkerer/issue/41
