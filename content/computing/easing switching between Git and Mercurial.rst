easing switching between Git and Mercurial
==========================================

:date: 2013-02-16
:tags: Python, VCS



For a long time I've been meaning to write a script that eases switching
between the only VCS systems I use, Mercurial and Git. Each chance I
get, I use Mercurial (e.g. personal stuff), and use Git when I don't
have much of a choice (e.g. FLOSS and work). That is, I use both quite a
lot, and too often I find myself running commands for one while on
another's repository.

I then decided to ease the pain my creating `a script`__ which checks which
VCS system I'm on, and displays the relevant command.
Here are the relevant aliases:

.. code-block:: sh

    alias vb='$(python ~/projects/utils/vcs.py --branch)'
    alias vd='$(python ~/projects/utils/vcs.py --diff)'
    alias vl='$(python ~/projects/utils/vcs.py --log)'
    alias vp='$(python ~/projects/utils/vcs.py --push)'
    alias vs='$(python ~/projects/utils/vcs.py --status)'
    alias vu='$(python ~/projects/utils/vcs.py --pull)'
    alias vc='$(python ~/projects/utils/vcs.py --commit)'
    alias vo='$(python ~/projects/utils/vcs.py --checkout)'
    alias vr='$(python ~/projects/utils/vcs.py --revert)'

Displaying the output instead of running them directly from the script
gives me the flexibility of adding to the command, for example:

.. code-block:: sh

    # committing
    vc 'describe the change'
    # checking history of a file
    vl README

This makes my life so much easier, since I no longer have to care where
I'm at, at least for the most common of commands. I am pleased with self.


__ https://bitbucket.org/tshepang/scripts/src/tip/vcs.py
