a bit of benchmarking
=====================

:date: 2013-10-26
:tags: Python



I was curious how my home machine performs compared to my work
machine. Each of these have 4 logical processors (and 8GB of RAM), so
are sort of comparable.

Some details for home machine::

   $ uname --all
   Linux thome 3.11-trunk-amd64 #1 SMP Debian 3.11-1~exp1 (2013-09-12) x86_64 GNU/Linux
   $ cat /proc/cpuinfo | sed --quiet '5p'
   model name      : Intel(R) Core(TM) i5-2410M CPU @ 2.30GHz

Some details for work machine::

   $ uname --all
   Linux twork 3.10-3-amd64 #1 SMP Debian 3.10.11-1 (2013-09-10) x86_64 GNU/Linux
   $ cat /proc/cpuinfo | sed --quiet '5p'
   model name      : AMD Phenom(tm) II X4 970 Processor

I ran two benchmarks, both from the latest VCS version of CPython, on
the ``default`` hg branch::

  $ hg tip
  changeset:   86643:af67cfcd4089
  tag:         tip
  user:        Tim Peters <tim@python.org>
  date:        Fri Oct 25 20:46:51 2013 -0500
  summary:     Issue #19399: fix sporadic test_subprocess failure.

* Building the latest VCS version of CPython:

  Command::

    make distclean; time (./configure && make --silent --jobs=4)

  Results for home machine::

    real    2m7.223s
    user    3m24.836s
    sys     0m9.840s

  Results for work machine::

    real    2m1.802s
    user    2m24.032s
    sys     0m12.180s

* Running the test suite:

  Command::

    time ./python -m test --multiprocess=0

  **--multiprocess=0** means that there will be 6 tests run in
  parallel; that is the number logical cores (4 in my case) + 2 (to
  avoid waiting too long for tests which are largely idle)

  Results for home machine::

    real    3m38.528s
    user    6m47.824s
    sys     0m30.220s

  Results for work machine::

    real    2m29.072s
    user    4m9.856s
    sys     0m26.428s

Just for kicks, I decided to check how long building Linux
would take; for this, I used latest 'final' release from Linus' git tree::

  $ git log -1
  commit 6e4664525b1db28f8c4e1130957f70a94c19213e
  Author: Linus Torvalds <torvalds@linux-foundation.org>
  Date:   Mon Sep 2 13:46:10 2013 -0700

  Linux 3.11

I also used the default menuconfig settings, and then ran
``make``. Here goes:

  Results for home machine::

    real    43m17.624s
    user    145m25.756s
    sys     9m9.104s

  Results for work machine::

    real    28m16.326s
    user    65m51.120s
    sys     5m35.364s

Note that the results for home machine may be skewed by the fact that
it kept getting throttled due to overheating. I only noticed this when
building Linux, which is a far more demanding task.

----

`Nice post on the meaning of the output`__


__ http://stackoverflow.com/a/556411/321731
