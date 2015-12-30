Sony Vaio Pro 13 (SVP13212SGBI)
===============================

:date: 2014-04-24
:tags: hardware



On **2014-02-13** I went to collect `the laptop`__ from `these
guys`__, which I paid around R12500 (~$1200) for. It's a 4GB RAM,
128GB SSD, FHD model. I would have happily paid for more RAM and
storage, but this seems the only model available in my home country. I
am glad that it's also not a touch screen... I don't need the
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

Issues
------

* The corners of the laptop are rather sharp,
  making it a little uncomfortable to handle.

* The power button is not so easy to press, and offers very little
  'feedback'... it has very shallow movement. Luckily there should not
  be a frequent need to use it, but there are times when something is
  buggy enough to cause OS hangs and other misbehaviour.

* The fan is too quick to kick in, and easily gets noisy. Running the
  following commands does not help, at least not in a way I could
  notice::

    echo silent | sudo tee  /sys/devices/platform/sony-laptop/thermal_control

  I don't know why this happens, given that I have never seen the
  temperature rise above 60 °C::

    $ sensors
    acpitz-virtual-0
    Adapter: Virtual device
    temp1:        +48.0°C  (crit = +97.0°C)

    coretemp-isa-0000
    Adapter: ISA adapter
    Physical id 0:  +48.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 0:         +46.0°C  (high = +100.0°C, crit = +100.0°C)
    Core 1:         +45.0°C  (high = +100.0°C, crit = +100.0°C)

* The screen brightness control is painful. It requires one to press
  the combination of the **Fn** key and **F5** (dim) and **F6**
  (brighten), which is fine. But one cannot just hold the two latter
  keys, but has to repeatedly press them to reach the desired
  result. That would not be such a big problem, except that it takes
  such a long time to get there... more than 50 presses from the two
  extremes!

* I still haven't got used to **Pg Up/Dn** and **Home/End** being
  accessible only via the **Fn** key. It's so awkward.

* The touchpad is a great pleasure to use, except when pressing and
  dragging. It's a hit-and-miss affair... you have to press quite
  hard, and that makes precise control challenging.

* The flexibility of the body results in keyboard marks on the screen.

* The worst problem, however, is the flexibility of at the bottom of
  the touchpad. Too often the touchpad fails to respond because I've
  put the thing at the wrong angle... I mostly use my laptop in bed.


__ http://www.youtube.com/watch?v=Xq-ZBke68tA
__ http://www.comx.co.za
__ https://wiki.archlinux.org/index.php/Sony_Vaio_Pro_SVP-1x21#Sound
__ http://tshepang.net/a-bit-of-benchmarking
