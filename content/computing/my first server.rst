my first server
===============

:date: 2013-10-10
:tags: Debian



The closest I ever came to needing own server is for hosting `my
blog`__, but I've had plenty of gratis services available to me, latest
being `GitHub Pages`__. When DigitalOcean__ `offered a $10 credit`__
(enough to buy two months of the most basic offering... 1 CPU core,
0.5GB RAM, 20GB storage), I thought why not.

As for the experience, I was quite impressed by the performance. It's
no wonder why the service receives so much praise from all over the
place; it's quite a lot for that ridiculous $5 fee. I've never
experienced storage this fast... my laptop has a hard-drive and the
SSD on my work machine is unimpressive. The CPU also appears powerful,
though I haven't stressed it yet.

I've spent the last few hours setting it up, after which I created a
snapshot, which is something to restore from in case of trouble. I
even destroyed and re-created it, just to make sure it works. This was
the second-worst experience playing with this service... it's so damn
slow! And by that, I mean destroying a Droplet (their name for the VM)
takes well over a minute, same as re-creating it. Maybe I'm being too
demanding, maybe it can't be helped, especially given the price, but
it's still slow as fuck.

What about the worst experience? It's the Console Access, which allows
for recovery in case of issues. It was painful to use since it's so
slow, and kept inserting wrong characters in place of the username. It
also tends to fail with the message::

  Failed to establish a connection to the console. Please reload.

It's not a big issue anyways, since this will be a rarely-used
feature.

And no, I still don't know yet what I'll use this for. Maybe I'll host
my blog there, moving it from the GitHub service. Regardless, it's
nice to have a machine accesible from anywhere on the web.


__ http://tshepang.net/tags.html#blogging-ref
__ http://pages.github.com
__ https://www.digitalocean.com/?refcode=25b4887810cc
__ http://thechangelog.com/107
