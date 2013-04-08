enjoying net connection at home, finally
========================================

:date: 2008-09-28
:tags: untagged



After suffering with being forced to access the net on Windows XP `for
over 2 weeks`_, I'm glad things turned out as I envisioned for I managed
to get my device working on Debian `with a lot of help`_. Here's what
went into my /etc/wvdial.conf:

.. code-block: ini

    [Dialer Defaults]
    Phone = #777
    Username = phone_number@neotel.co.za
    Password = 1234
    Stupid Mode = 1
    Dial Command = ATDT

    [Dialer neotel]
    Modem = /dev/ttyUSB0
    Baud = 460800
    Modem Type = Analog Modem
    Stupid Mode = 1

I had to run ``sudo modprobe usbserial vendor=0x1d09 product=0x4000``
and then ``sudo wvdial neotel`` afterwards and then I lived happily for
long...

Now why is XP so uncomfortable? I'm used to many of the conveniences of
Debian that are absent in XP or I'm not motivated to find replacements for
stuff like workspaces, copy-text-on-highlight, Epiphany, Quod Libet,
debmirror, Nautilus, ...


.. _for over 2 weeks: http://tshepang.net/net-connection-at-home-finally
.. _with a lot of help: http://mybroadband.co.za/vb/showthread.php/129619-Neotel-working-on-Linux!
