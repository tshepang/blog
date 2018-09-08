---
date: '2012-06-09'
tags: 'developer-of-note, Python'
title: 'developer of note: Victor Stinner'
---

Depending on the change, contributing to open source software can be
intensely challenging. Referring specifically to CPython, the reference
implementation of my favorite programming language, you can have
hundreds of messages on the mailing lists, and at times, many more in
the issue tracking system, all discussing the change in mind. Such
changes are most often accompanied with a [PEP] (Python Enhancement
Proposal), a document which is basically a design spec for such a
change. It also, helpfully, summarises the arguments against the change,
and addresses them while at it.

Given all that, it can be quite challenging for any one individual to
champion such important changes, and an example of one such heroic
individual is [Victor Stinner], a core CPython developer. He is the most
visible of the guys who helped ensure acceptance of [PEP 418], which
proposes some time-related additions and improvements to the standard
library\'s [time module]. The sheer amount of discussion that went
around this particular PEP was ridiculous. The mailing list discussions
were practically endless, and so were the updates to the PEP, not to
mention the amount of research involved, which was needed in order to
have CPython expose this functionality in a cross-platform manner. Now,
that\'s some serious perseverance.

In addition to this work, the guy has done a heck of a lot of work in
cleaning up, re-factoring, and optimizing the string-handling code. I
can\'t imagine that this stuff is easy, especially since a large portion
of it is in C! There\'s a whole lot more work he has done\... he\'s
among the most prolific of all core CPython developers.

  [PEP]: http://www.python.org/dev/peps/pep-0001/
  [Victor Stinner]: http://www.haypocalc.com/wiki/Accueil
  [PEP 418]: http://www.python.org/dev/peps/pep-0418/
  [time module]: http://doc.python.org/library/time
