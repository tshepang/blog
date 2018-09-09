+++
date = 2011-03-26
tags = ['Python', 'GNOME']
title = "cleansing multiple build directories"
+++

In my adventures of [building GNOME with JHBuild], it often happens that
when I tweak something that affects the build environment (e.g. use
system Python instead of JHBuild-built one), I get a heck of a lot of
build failures. This will happen even after I run jhbuild clean (which
runs `make clean` on the modules), testimony to the weakness ofthe GNOME
build infrastructure (autotools, \...). This means that I need to run
`make distclean` or better still (where applicable) `git clean -dfx`.
Note that I sometimes even have to uninstall one or two modules (on
JHBuild path) to get a build failure fixe
(`jhbuild uninstall modulename`). This is laborious work, so I sometimes
just wipe out the entire installation.

Note that there\'s dozens of modules to build, so I wrote this little
script to take care of it:

``` {.sourceCode .python}
import os
import subprocess
top_level = os.path.expanduser("~/src/gnome")
for filename in os.listdir(top_level):
    full_path = "{}/{}".format(top_level, filename)
    if os.path.isdir(full_path):
        cmd = "cd ~/src/gnome/{} && git clean -dfx".format(filename)
        if subprocess.call(cmd, shell=True) != 0:
            cmd = "cd ~/src/gnome/{} && make distclean".format(filename)
            if subprocess.call(cmd, shell=True) != 0:
                cmd = "cd ~/src/gnome/{} && make clean".format(filename)
                subprocess.call(cmd, shell=True)
```

update
======

Someone very kind guy made [a bunch of suggestions], making my code much
better:

``` {.sourceCode .python}
import os
import subprocess
top_level = os.path.expanduser("~/src/gnome")
for filename in os.listdir(top_level):
    full_path = os.path.join(top_level, filename)
    if os.path.isdir(full_path):
        os.chdir(full_path)
        if subprocess.call("git clean -dfx".split()) != 0:
            if subprocess.call("make distclean".split()) != 0:
                subprocess.call("make clean".split())
```

further reading
===============

modules: [os], [os.path], [subprocess]

  [building GNOME with JHBuild]: http://tshepang.net/my-jhbuild-setup
  [a bunch of suggestions]: http://codereview.stackexchange.com/questions/1476/cleansing-multiple-build-directories/1477#1477
  [os]: http://docs.python.org//library/os
  [os.path]: http://docs.python.org//library/os.path
  [subprocess]: http://docs.python.org//library/subprocess
