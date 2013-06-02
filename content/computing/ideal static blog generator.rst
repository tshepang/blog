ideal static blog generator
===========================

:date: 2013-05-12
:tags: blogging


Anything not listed below is either stuff I take for granted or simply
missed:

* reStructuredText__ support is mandatory, and so is being written in
  Python (I is a fanboy).

* 3 alternatives for the Landing Page:

  - The latest post should be displayed in its entirety, and the rest
    displayed in an Archive view below it (so one can quickly search
    all post Titles without leaving that page).
  - It should be an About Page.
  - It should present Archive View.

* Categories should be determined by directory into which a post is
  placed if not explicitly specified (in file metadata section).

* Ability to determine post date from file mtime.

* Post Date should always precede post content.

* An option to have clean urls (i.e. trailing ``.html`` removed).

* Date-based directory structure should not be mandatory (`unlike with
  Tinkerer`__).

* Inline literals and literal blocks (for code) should be
  distinguished by background colour; using different fonts is not
  good enough.

* Tags (and maybe Categories) should be displayed on each post.

* An feed icon that is visible from landing page (and maybe Category
  pages).

* Blogofile has a strange requirement of having `post headers be YAML
  format`__. Maybe there's a good reason, but I want my generator to
  not require anything special in file contents.


__ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
__ https://bitbucket.org/vladris/tinkerer/issue/41
__ http://docs.blogofile.com/en/latest/posts.html
