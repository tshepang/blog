+++
date = 2014-10-30
title = "impressed by the ease of creating Upstart jobs"

[taxonomies]
tags = ['non-Debian']
+++

At work, we run our systems on Ubuntu, which so far means the init
system is Upstart. I needed to have one binary to start when the system
boots, and because I'm horrified by sysvinit scripts (which Upstart
supports), I decided to give creating an Upstart job a try. I was
surprised how easy it was:

    exec /usr/local/bin/executable
    start on startup
    respawn

I placed a file with above contents in `/etc/init/executable.conf`, and
that's pretty much it. Impressive.

Here's what happens:

-   `exec` instructs Upstart what executable to run
-   `start on` is an instruction on when to start the service
-   `respawn` means the service should re-start if ever it dies for some
    reason

One convenient thing that's happening is that stdout output of the
service gets re-directed to a log file, in this case
`/var/log/upstart/executable.log`. Cool stuff.

I found help from [Getting Started] and [the Cookbook].

  [Getting Started]: http://upstart.ubuntu.com/getting-started.html
  [the Cookbook]: http://upstart.ubuntu.com/cookbook
