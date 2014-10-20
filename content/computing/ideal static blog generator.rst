ideal static blog generator
===========================

:tags: blogging


Anything not listed below is either stuff I take for granted or simply
missed:

* reStructuredText__ support is mandatory, and so is being written in
  Python (I is a fanboy).

* Ordered by preference:

  - The latest post should be displayed in its entirety, followed by
    an Archives View (just Post title and date) or a subset
    (i.e. Recent Posts).
  - It should be an Archives View (or a subset).
  - It should be an About Page.

* Categories should be determined by directory into which a file (the
  raw material for a Post) is placed. Specifying this in the metadata
  section of the file should of course take precedence.

* Publish date should never be placed at the bottom of a Post. It is
  too important a piece metadata to treat this way.

* An option to have clean urls (i.e. trailing ``.html`` removed).

* Date-based directory structure should not be mandatory (unlike with
  Tinkerer).

* Inline literals and literal blocks (for code) should be
  distinguished by background colour; using a different font is just not
  good enough.

* Tags (and maybe Categories) should be displayed on each post.

* A feed icon that is visible from the main page (and maybe Category
  pages).

* Blogofile has a strange requirement of having `post headers be YAML
  format`__. Maybe there's a good reason, but I want my generator to
  not require anything special in file contents.

* (minor) Ability to determine Publish date from file mtime


__ http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
__ http://docs.blogofile.com/en/latest/posts.html
