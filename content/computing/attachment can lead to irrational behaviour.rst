attachment can lead to irrational behaviour
===========================================

:date: 2012-02-01
:tags: Debian, non-Python



In `my previous job`_, we used to use some Java framework, `Mule ESB`_,
for our clients. The project is distributed with a lot of jar files,
supposedly for the convenience of users. When we work on a project, we
just add all those jars to the classpath (we use Eclipse, an excessively
powerful and ugly IDE). Now, me being a sucker for the Debian way of
doing things, I'd install packages providing all those jars from a
Debian repository, then remove those Mule-distributed files, then add
symlinks in place of them pointing back to the actualy files. Imagine
how much time it took! Either that, or even easier (but still
time-consuming), skip the symlink thing entirely and just add those jars
(found in **/usr/share/java** directory) directly.

Beyond just wasting time, the are other potential problems with my
approach:

-  Debian's jar versions did tend to be different to Mule-supplied
   versions. You can imagine what problems this can cause, especially
   because the versions included there are most likely the ones used for
   testing Mule.
-  Even if the versions were the same, what if there are slight changes
   from Debian's side. Debian's strict `software guidelines`_ implies
   that they'll strip out some stuff that doesn't adhere. The good thing
   is that Debian appends ``dfsg`` to the version number, but `not
   everybody knows that`_. And even if they did, they would then need to
   spend time checking exactly what changed.
-  Debian doesn't merely re-distribute the jar files. They actually
   rebuild them, with Debian-supplied compilers. Maybe this isn't an
   issue for Java projects, but who knows.

This is not to knock the Debian way of doing things. It's actually quite
excellent (hence my love), but it can't fit all scenarios. See Matt
Zimmerman's `excellent post`_, where he touches on this issue.

I did wise up a bit by simply doing things the way the makers of Mule
intended.

.. _my previous job: http://tshepang.net/me-got-meself-a-coding-job
.. _Mule ESB: http://www.mulesoft.org/
.. _software guidelines: http://www.debian.org/social_contract#guidelines
.. _not everybody knows that: http://askubuntu.com/q/11592/2591
.. _excellent post: http://mdzlog.alcor.net/2010/07/06/weve-packaged-all-of-the-free-software-what-now/
