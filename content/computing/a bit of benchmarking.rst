a bit of benchmarking
=====================

:date: 2013-10-27
:tags: Python
:summary: comparing performance of my laptop and my work machine



I was curious how my home machine performs compared to my work
machine. Each of these have 4 logical processors (and 8GB of RAM), so
are sort of comparable. I also added the `DigitalOcean`__ VPS with
those specs (`currently $80 per month`__) because... why not.


Machine Specs
-------------

Each machine runs Debian testing (codename "jessie"). Following is the
output of these commands for each machine::

  uname --all
  cat /proc/cpuinfo | sed --quiet '5p'

Home machine::

  Linux thome 3.11-trunk-amd64 #1 SMP Debian 3.11-1~exp1 (2013-09-12) x86_64 GNU/Linux
  model name      : Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz

Work machine::

  Linux twork 3.10-3-amd64 #1 SMP Debian 3.10.11-1 (2013-09-10) x86_64 GNU/Linux
  model name      : AMD Phenom(tm) II X4 970 Processor

DigitalOcean VPS::

  Linux tcloud 3.11-1-amd64 #1 SMP Debian 3.11.5-1 (2013-10-17) x86_64 GNU/Linux
  model name      : QEMU Virtual CPU version 1.0


CPython benchmarks
------------------

I ran two benchmarks, both from the latest VCS version of CPython,
development branch::

  $ hg identify --id --branch
  b6a1a78818fe default


Build
^^^^^

Here's the command I used::

  make distclean; time (./configure && make --silent --jobs=4)


Results
*******

Home machine::

  real    2m11.687s
  user    3m18.104s
  sys     0m9.964s

Work machine::

  real    2m2.707s
  user    2m24.200s
  sys     0m12.280s

VPS::

  real    2m30.931s
  user    3m7.272s
  sys     0m16.592s

Test suite
^^^^^^^^^^

Here's the command I used::

  time ./python -m test --multiprocess=0

**--multiprocess=0** means that there will be 6 tests run in parallel;
that is the number logical cores (4 in my case) + 2 (to avoid waiting
too long for tests which are largely idle)


Results
*******

Home machine::

  real    3m42.571s
  user    7m13.124s
  sys     0m33.320s

Work machine::

  real    2m29.957s
  user    4m9.052s
  sys     0m27.364s

VPS::

  real    2m19.174s
  user    5m5.444s
  sys     0m40.008s


Linux kernel build
------------------

Just for kicks, I decided to check how long building Linux would take;
for this, I used latest 'final' release from Linus' git tree::

  $ git log -1
  commit 6e4664525b1db28f8c4e1130957f70a94c19213e
  Author: Linus Torvalds <torvalds@linux-foundation.org>
  Date:   Mon Sep 2 13:46:10 2013 -0700

  Linux 3.11

Here's the commands I used::

  make distclean && make defconfig && time make


Results
^^^^^^^

Home machine::

  real    6m11.622s
  user    21m2.664s
  sys     1m15.324s

Work machine::

  real    2m40.275s
  user    8m55.624s
  sys     0m42.860s

VPS::

  real    3m41.240s
  user    12m21.120s
  sys     1m17.844s

Conclusion
----------

My work machine is faster than the DigitalOcean offering of comparable
specs, and much faster than my home machine, a laptop.

(`detailed explanation of the output`__)


__ https://www.digitalocean.com/?refcode=25b4887810cc
__ https://www.digitalocean.com/pricing
__ http://stackoverflow.com/a/556411/321731
