moving from Acer TravelMate to HP Probook, using Debian
=======================================================

:date: 2011-07-16
:tags: Debian, hardware



I have been using an Acer TravelMate 6592 laptop for close to 3 years
(ever since I got `my coding job`_). It had some issues:

-  `it's damn ugly`_, though not as much as Lenovo ones
-  it requires Intel non-free firmware for its Wi-Fi chipset
-  it frequently refused to make the LAN accessible from Linux on boot;
   this was likely a BIOS issue
-  the battery capacity was below 50% so it didn't last
-  the hard drive was developing bad sectors

Other than that, it truly was an excellent laptop, and I never
complained about its performance, ever since I added a 2GB RAM stick, to
make it a total of 4GB (except that I wished my HDD was faster, tempting
me to buy an SSD). What else I really liked about it is the
feature-packed touchpad: Beyond the normal two-finger and
side-scrolling, it also had up-down-left-right buttons which allowed
constant-speed scrolling. It's interesting that such a touchpad is very
rare.

I now got an HP Probook 4530s and its pros:

-  `it's stunning`_
-  it's got a real fast hard drive; there were times when I saw speeds
   upwards to 70MB/s, which I never saw with the older laptop
-  its Wi-Fi doesn't require non-free software
-  it's far more modern (USB3 support) and supposedly faster (Core
   i5-2410M vs. Core 2 Duo T7500), but my typical workload made even the
   TravelMate more than adequate

And the cons:

-  a less featureful touchpad
-  keyboard keys placed in weird locations (e.g. **pg up** and **pg dn**
   buttons are placed far away, at the top-right corner; I blame the
   (needless for me) numeric keypad
-  the screen resolution is on the low side and so is the screen size;
   the older laptop is much bigger even if they are both labeled 15.4"

...and Debian:

Quite a few times, I tend to want to stick to a stable release of
Debian. Following Debian development does take time (frequent updates,
curiosity to see what changed, and something getting broken here and
there). So I tried to do the same here. Sadly, some of the software in
Squeeze is too outdated to be optimal, so am glad to have teams like
`Debian Backports folk`_. But that wasn't enough, so I ended up
installing Xorg components from Debian Unstable (Suspend doesn't work
well with Squeeze (Debian 6) and backports doesn't have a newer X
version.

Let's see how long I last trying to keep pure by running as little from
outside Squeeze as possible.

**update**:

This didn't even last for 1 day. I was having issues with my X hanging
the entire OS, forcing me to do a hard-reboot. This happened when I was
watching a video using VLC, so I blamed it and installed the version
from Debian Unstable. Sadly, doing things that way resulted in a VLC
that refused to die normally, forcing me to do ``kill -9 vlc``. I then
just screwed my plans and upgraded fully to Unstable, and now VLC quits
gracefully. Let's see if I'll have the X lockup again.

**update 2**:

Well, I still experience machine lock-ups, the bad ones forcing a
hard-reboot. This might be related to Wi-Fi because I used the system
for quite a while using the wired link, without any such lock-up.

**update 3**:

No more lock-ups, except very rarely. I run a mix of Testing and
Unstable at the moment, but my "/etc/sources.list" file points solely at
my custom repository and Testing, for it just is tiring to keep tracking
Unstable... way too much bandwidth.

.. _my coding job: http://tshepang.net/me-got-meself-a-coding-job
.. _it's damn ugly: http://www.google.co.za/search?hl=en&biw=1366&bih=630&q=6592+acer&um=1&ie=UTF-8&tbm=isch&source=og&sa=N&tab=wi
.. _it's stunning: http://www.google.co.za/search?q=probook+4530s&um=1&ie=UTF-8&tbm=isch&source=og&sa=N&hl=en&tab=wi&biw=1366&bih=630
.. _Debian Backports folk: http://tshepang.net/thanks-to-the-debian-backports-team
