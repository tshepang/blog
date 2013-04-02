easing switching between Git and Mercurial
==========================================

:date: 2013-02-16
:tags: Python



For a long time I've been meaning to write a script that eases switching
between the top 2 DVCS systems, Mercurial and Git. You, each chance I
get, I use Mercurial (e.g. personal stuff), and use Git when I don't
have much of a choice (e.g. FLOSS, work). That is, I use both quite a
lot, and very often I find myself running commands for one while on
another's repository. I then decided to ease the pain: `source code`_.

This makes my life so much easier, since I no longer have to care where
I'm at, at least for the most common commands.

I also happen to be a bash alias junkie. I have close to 200, though I
tend to forget that many exists as time passes. Anyways, you will notice
that the above script just prints out the command, so I run those from
my aliases:

.. code-block:: sh

    alias vb='$(python ~/projects/utils/vcs.py --branch)'
    alias vd='$(python ~/projects/utils/vcs.py --diff)'
    alias vl='$(python ~/projects/utils/vcs.py --log)'
    alias vp='$(python ~/projects/utils/vcs.py --push)'
    alias vs='$(python ~/projects/utils/vcs.py --status)'
    alias vu='$(python ~/projects/utils/vcs.py --pull)'
    alias vc='$(python ~/projects/utils/vcs.py --commit)'
    alias vo='$(python ~/projects/utils/vcs.py --checkout)'

I am pleased with self.

.. _source code: https://bitbucket.org/tshepang/scripts/src/tip/vcs.py
