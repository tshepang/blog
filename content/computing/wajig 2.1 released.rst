---
date: '2011-04-27'
tags: 'Debian, wajig'
title: 'wajig 2.1 released'
---

Today I released [a new version of wajig], first time in about half a
year. It\'s not even like there\'s some major stuff or anything; I just
haven\'t put as much time. Regardless, it\'s quite a good release.

One of the changes is getting rid of gjig, the GUI interface.

-   I actually did like it, but it was never a production standard piece
    of code. It was actually quite nifty and useful, but the interface
    was not at all modern or usual. It also needed a lot of polish.
-   I learned a lot from trying to port it away from the deprecated
    libglade library to a more modern gtkbuilder (part of GTK+). But the
    porting documentation wasn\'t really good, so I was left with the
    option of doing it from scratch\... not exactly a small task.
-   Worse still is the fact that there were more pro-looking GUI package
    managers out there.
-   It didn\'t keep up with the pace of development wajig. It was a
    2nd-class citizen.
-   Oh, and I\'m so afraid of GUI developement, or should I say GTK+. It
    was never an easy domain for me, and I still don\'t really get it.
    And yes, I\'ve tried. Maybe other toolkits are easier, and I\'m too
    lazy to check them out.
-   I wanted to move wajig forward into Python 3 land, and given that
    GTK+ support for that Python version isn\'t exactly mature (at time
    of writing), I felt that I was being held back.

  [a new version of wajig]: http://packages.qa.debian.org/w/wajig/news/20110427T131707Z.html
