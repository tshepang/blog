project of note: git-cola
=========================

:date: 2012-08-17
:tags: project-of-note



A colleague has since introduced the tool for me, and I use it whenever
I want to do separate commits for uncommited changes, to avoid having to
do the unkool ``git add <filename> && git commit`` dance. I also use it
when I want to commit various hunks separately, and the tool makes that
task real easy.

I was recently impressed by its equivalent functionality for the git
``--amend`` option. If you click on the **Amend Last Commit** radio
button, it actually displays the commit message of that previous commit.
I was surprised to see it, especially since on clicking that option, I
quickly ran to the command-line to copy that commit message, only to see
the message waiting for me, ready to be edited away.

Another feature I really like is that if you attempt to commit something
without staging it first, instead of just complaining, if offers to
*stage and commit* all in one click. Nice.

These functionalities are real simple, but they really make for a
pleasant user experience.

--------------

When I checked its Debian PTS page, I got surprised by the glaring lack
of bug reports, as well as a small number of Debian releases. I found it
sad when I visited it's `popcon page`_ (which is linked from that PTS
page), and got surprised by the low number of installations it has by
Debian users.

.. _popcon page: http://qa.debian.org/popcon.php?package=git-cola
