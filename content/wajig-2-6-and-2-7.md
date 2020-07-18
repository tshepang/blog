+++
date = 2012-07-02
title = "wajig 2.6 and 2.7"
[taxonomies]
tags = ['wajig', 'Debian']
+++

Version 2.6 of wajig has changes so small that I did not bother writing
about its release, but was nevertheless very important because the
bash-completion now works a lot better than before, thanks to [Reuben
Thomas]. I also stopped wajig from accepting UPPERCASE subcommands,
since a few people on the mailing list expressed dislike, and that
includes project founder.

Version 2.7, the version that will be in the next stable release of
Debian [[update]], Wheezy (Debian 7), fixes two bugs, one of which I
sort of intentionally broke in order to fix some issues with the
`--simulate` and/or `--teaching` options. Someone [did complain about
this] which was good since it's a good indicator that someone actually
cared about the feature. That motivated me to fix it, and I ensured that
the fix was in before Debian 7 freeze.

This work is my greatest contribution for this upcoming Debian release.

  [Reuben Thomas]: http://rrt.sc3d.org/
  [update]: @/debian-7-will-release-with-wajig-2-7-3.md
  [did complain about this]: http://bugs.debian.org/670687
