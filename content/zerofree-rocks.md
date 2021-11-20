+++
date = 2015-01-15
title = "zerofree rocks!"
[taxonomies]
tags = ['untagged']
+++

At work, we tend to use the same base image for multiple installations.
I would often copy a whole-disk image of a system as a matter of
convenience, because that way I only need to `dd` to the target, without
any additional steps. The problem with this approach is that it is
slower than taking a tarball of the files (from the source) and
extracting them onto the target. That's because it works with a lot
more data than it needs. For example, say you have a 4GB disk which is
only filled with 1GB data. The first method would mean that processing a
useless 3GB of one and zeroes, but my main concern is that the
whole-disk doesn't compress well. So here's what I tried after
creating a tarball:

-   Simple file removal and extraction
    (`cd /target && rm -r * && tar xf ~/rootfs.tar`) didn't work
-   Re-formatting the drive (`mkfs.ext4 /dev/mmcblkp1`) and then
    extraction didn't work either

The issue is that with the 2 steps above, there still remains much data
on the partition from previous use. That is, file removal and creating a
filesystem doesn't remove the actual data, but rather just makes the
data inaccessible by conventional means. To the data compressor (`xz` in
this case), that is all valid data. What needs to happen is for the data
that is not allocated to be over-written with zeroes... enter
[zerofree] which does just that. After it was done, my compressed image
shrunk from ~400MB to ~80MB. The original was about 2GB.

  [zerofree]: https://packages.debian.org/sid/zerofree
