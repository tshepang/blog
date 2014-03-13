Sony Vaio Pro 13 (SVP13212SGBI)
===============================

:date: 2014-02-19
:tags: hardware



On **2014-02-13** I went to collect `the laptop`__ from `these
guys`__, which I paid around R12500 (~$1200) for. It's a 4GB RAM,
128GB SSD, FHD model. I would have happily paid for more RAM and
storage, but this seems the only model available in my home country. I
am glad that it's also not a touch screen. I don't need that kind of
reflection.

Anyways, there was much pain involved trying to get it to work. I
struggled to get Debian booting, and I don't know what I did wrong
because after a few attempts of trying this and that, things
worked. And man, that SSD is fast: it takes 6-7 seconds to GUI login
screen. Package installation is also insane fast.

There was much pain trying to get audio to work. Luckily `I got some
help`__, where I needed to change two lines in
`/usr/share/alsa/alsa.conf`::

  defaults.ctl.card 1
  defaults.pcm.card 1

VLC video didn't work well either, but I
needed only change Video Output to **OpenGL GLX video output (XCB)**,
and all was well.

Performance
-----------

I am now going to check how this machine compares to `these others`__.

Specs::

  $ uname --all
  Linux thome 3.12-1-amd64 #1 SMP Debian 3.12.9-1 (2014-02-01) x86_64 GNU/Linux
  $ cat /proc/cpuinfo | sed --quiet '5p'
  model name      : Intel(R) Core(TM) i5-4200U CPU @ 1.60GHz

CPython build (changeset ``b6a1a78818fe``)::

  $ make distclean; time (./configure && make --silent --jobs=4)
  [...]
  real    1m52.372s
  user    3m12.460s
  sys     0m6.764s

CPython test suite::

  $ time ./python -m test --multiprocess=0
  [...]
  real    3m34.582s
  user    5m12.260s
  sys     0m20.640s

Linux kernel build (commit ``6e4664525b1d``)::

  $ make distclean && make defconfig && time make
  [...]
  real    11m57.220s
  user    11m1.544s
  sys     0m38.260s


So the machine still doesn't compare with my work machine, a ~2
year-old desktop. It is faster than my old laptop as expected, and
comparable to the DigitalOcean VPS, no surprises there. The storage is
a lot faster though... I've seen sustained read speeds of ~500MB/s.


__ http://www.youtube.com/watch?v=Xq-ZBke68tA
__ http://www.laptopdirect.co.za/Sony-VAIO-SVP-13212SGBI-lp-78188.php
__ https://wiki.archlinux.org/index.php/Sony_Vaio_Pro_SVP-1x21#Sound
__ http://tshepang.net/a-bit-of-benchmarking
