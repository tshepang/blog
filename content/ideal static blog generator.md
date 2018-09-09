+++
tags = ['blogging']
title = "ideal static blog generator"
date = 2015-01-11
+++

Anything not listed below is either stuff I take for granted or simply
missed:

-   [reStructuredText] support is mandatory. It\'s the only markup
    language I like.
-   Landing Page should be an Archives View (Post title and date) or a
    subset (i.e. Recent Posts). I would not mind if the latest Post or
    the About Page were displayed, so long as they are followed by this
    Archives View.
-   Categories should be determined by directory into which a file (the
    raw material for a Post) is placed. Specifying this in the metadata
    section of the file should of course take precedence.
-   Publish date should never be placed at the bottom of a Post. It is
    too important a piece metadata to treat this way.
-   An option to have clean URLs (i.e. trailing `.html` removed).
-   Date-based directory structure should not be mandatory (unlike with
    Tinkerer).
-   Inline literals and literal blocks (for code) should be
    distinguished by background colour; using a different font is just
    not good enough.
-   Tags (and maybe Categories) should be displayed on each post.
-   Blogofile has a strange requirement of having [post headers be YAML
    format]. Maybe there\'s a good reason, but I want my generator to
    not require anything special in file contents.
-   Ability to determine Publish date from file mtime.

**nice-to-have**:

-   Ability to combine multiple tags.
-   Ability to show posts linking to current one, but I\'m not sure how
    useful this would be though.
-   A feed icon that is visible from the main page (and maybe Category
    pages).

  [reStructuredText]: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
  [post headers be YAML format]: http://docs.blogofile.com/en/latest/posts.html
