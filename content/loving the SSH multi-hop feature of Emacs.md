+++
date = 2014-09-04
title = "loving the SSH multi-hop feature of Emacs"

[taxonomies]
tags = ['Emacs']
+++

I\'m at home and want to access some system at work. I cannot access
this system directly, so will have to use a VPN or sshfs, but I don\'t
know how to set VPN up and sshfs feels rather clunky (I first have to
have some directory I\'m going to mount the thing, and have to remember
the command line syntax). With Emacs, I run the following command:

    C-x C-f /ssh:work|ssh:10.0.0.107|ssh:10.0.0.148:~/some/files/

What happens there is I ask Emacs to run `find-file`, which opens its
file manager, **Dired**. It first accesses the server at work, then my
work desktop (`10.0.0.107`), and then some machine (`10.0.0.148`) which
I normally access via my work desktop (it got SSH keys). Finally, I\'m
then presented with the view of the files in `~/some/files/` in that
machine, which I can work on (view, edit, save) like any local file. I
was surprised such a feature exists, thinking I\'d have to do ugly
things like port forwarding. I do use the single hop a lot (if that\'s
even the right name):

    C-x C-f /ssh:work:~/some/files/

Shortcut for that is:

    C-x C-f /work:~/some/files/

**sidenotes**:

-   The shortcut doesn\'t work with multi-hop
-   I love the fact that Emacs accepts SSH settings, where for example,
    instead of specifying the whole <username@host>, it accepts the
    aliases in `~/.ssh/config`, such that I only have to run:

        ssh work

    instead of:

        ssh tshepang@hostname
