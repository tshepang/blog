---
date: '2013-10-03'
tags: blogging
title: from Pelican to liquidluck
---

**notes**:

-   This post was first published on **2012-07-05**, which is shortly
    after I started using [liquidluck].
-   I have since moved back to Pelican on **2013-09-29**, with [Elegant
    theme]. Reason: slow liquidluck development ([the author is busy
    with other projects]), though he has more recently been doing [some
    large changes in a branch], which I assume is not ready. There is
    also [a backlog of doc improvements] I submitted, which are not even
    acknowledged. Do not consider this a complaint\... the author in
    fact gave me more than I gave him\... a nice piece of software. In
    fact, I might go back at some point, and will keep maintaining [live
    demos of the various liquidluck themes]. Also, [my movie blog] is
    also still built with liquidluck.
-   I have a separate post on [what I love about static website
    generators].

why [Pelican] rocks
===================

-   It has categories ([unlike nikola])
-   Post metadata:
    -   if Date is not specified, file mtime is used (unlike
        [blogofile])
    -   if Category is not specified, parent directory name is used
        (unlike blogofile)
    -   titles are allowed to have any character (unlike blogofile)
    -   there is an option to provide clean urls\... remove trailing
        `.html`
-   Does not force one into having ugly date-based filesystem structure
    (unlike [Tinkerer])

why Pelican rocks not
=====================

The default theme simply didn\'t fit my tastes, and [the other themes
weren\'t so satisfactory]. I spent way too long fiddling with them, and
just couldn\'t be happy.

why liquidluck
==============

So I have moved to [liquidluck], and am hoping I will not be \'forced\'
to move again. It\'s way too much work, and it took multiple messages
between me and [the developer] of this sleek new static site generator
just to get it to behave the way I like it.

I had to override stuff that\'s done by the software, by using [this
script], which helped give it the advantages that Pelican has over the
other generators I mentioned, while also solving the one problem Pelican
has.. lack of a good-enough theme. This was achieved with the help of
that very helpful and responsive developer.

issues
======

-   There is no visible way, at least for the default theme, to
    subscribe to RSS feeds of individual Categories.
-   The text is a bit blurry/faint with the default theme, and none of
    [the other ones][live demos of the various liquidluck themes] are
    close to good-enough for my liking, all but the promising one named
    [responsive]. It got 2 issues so far (see [live demo]):
    -   Date is displayed at the bottom of a post\... why make user
        scroll that far before presenting such a key piece of info.
    -   There is no link anywhere allowing to visit Home.
-   Background color for `<code>` text is too unusual, and results in an
    ugly look. It does not fit with the general general theme, so should
    be grey really, which would match with that of `<pre>` text. I fixed
    it myself with the following patch:

        diff --git a/liquidluck/_themes/default/static/style.css b/liquidluck/_themes/default/static/style.css
        index e90de80..94fa7e8 100644
        --- a/liquidluck/_themes/default/static/style.css
        +++ b/liquidluck/_themes/default/static/style.css
        @@ -112,7 +112,7 @@ pre {
             border-radius: 3px;
         }
         code, tt {
        -    background-color: #fee9cc;
        +    background-color: #eee;
             color: rgba(0, 0, 0, 0.75);
             padding: 1px 3px;
             font-size: 12px;

  [liquidluck]: http://liquidluck.readthedocs.org
  [Elegant theme]: http://oncrashreboot.com/pelican-elegant
  [the author is busy with other projects]: https://github.com/lepture/liquidluck/issues/101
  [some large changes in a branch]: https://github.com/lepture/liquidluck/issues/104#issuecomment-22825084
  [a backlog of doc improvements]: https://github.com/lepture/liquidluck/issues/created_by/tshepang?sort=updated&state=open
  [live demos of the various liquidluck themes]: http://tshepang.net/looking-at-liquidluck-themes
  [my movie blog]: http://movies.tshepang.net
  [what I love about static website generators]: http://tshepang.net/what-me-loves-about-static-website-generation
  [Pelican]: http://pelican.readthedocs.org
  [unlike nikola]: https://github.com/getnikola/nikola/issues/163
  [blogofile]: http://blogofile.com
  [Tinkerer]: http://tinkerer.me
  [the other themes weren\'t so satisfactory]: http://tshepang.net/favorite-pelican-themes
  [the developer]: http://lepture.com
  [this script]: https://bitbucket.org/tshepang/blog/src/1602cdf8/custom.py
  [responsive]: https://github.com/bingdian/liquidluck-theme-responsive
  [live demo]: http://demo-responsive.tshepang.net
