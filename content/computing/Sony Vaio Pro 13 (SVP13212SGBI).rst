Sony Vaio Pro 13 (SVP13212SGBI)
===============================

:date: 2014-02-16
:tags: hardware



On **2014-02-13** I went to collect `the laptop`__, which I paid
around R12500 for (~$1200). It's a 4GB RAM, 128GB SSD, FHD model. I
would have happily paid for more RAM and storage, but this seems the
only model available in my home country. I am glad that it's also not
a touch screen. I don't need that kind of reflection.

Anyways, there was much pain involved trying to get it to work. I
struggled to get Debian booting, and I don't know what I did wrong
because after a few attempts of trying this and that, things
worked. And man, that SSD is fast: it takes 6-7 seconds to GUI login
screen. Package installation is also insane fast.

There was much pain trying to get audio to work. Luckily `I got some
help`__, where I needed to change two lines in
`/usr/share/alsa/alsa.conf`. VLC video didn't work well either, but I
needed only change Video Output to **OpenGL GLX video output (XCB)**,
and all was well.


__ http://www.laptopdirect.co.za/Sony-VAIO-SVP-13212SGBI-lp-78188.php
__ https://wiki.archlinux.org/index.php/Sony_Vaio_Pro_SVP-1x21#Sound
