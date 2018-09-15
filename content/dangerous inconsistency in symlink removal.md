+++
date = 2011-01-28
title = "dangerous inconsistency in symlink removal"

[taxonomies]
tags = ['untagged']
+++

Here's how to make a symlink and to delete it:

``` {.sourceCode .sh}
mkdir dir
ln -s dir dirlink
rm -r dirlink
```

Here's another way to delete it:

``` {.sourceCode .sh}
rm -r dirlink/
```

Although it will do the job, it will actually complain with:

``` {.sourceCode .sh}
rm: cannot remove `dirlink': Not a directory
```

Note that we could have achieved the deletion with just:

``` {.sourceCode .sh}
rm dirlink
```

This is because the symlink is just a single file. So there's no need
to treat it like a directory when deleting.

Sadly, this behaviour is inconsistent when there is a mounted voulem.
The first way of deletion has no problem, but the second one will wipe
out the entire drive, if it so happens that `dir` is the mount directory
(i.e. `ln -s /media/my_drive dirlink && rm -r dirlink/`). I learned this
the hard way :(

[**sidenote**] Here's [some explanation].

  [some explanation]: http://unix.stackexchange.com/q/6618/688
