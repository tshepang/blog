it's less work building from a VCS than from a tarball
======================================================

:date: 2010-11-20



tarball:

1. find the website
2. find download link
3. download the tarball
4. navigate to the tarball (using a GUI file browser)
5. extract the tarball (using a GUI extractor)
6. navigate to the extracted directory (using the shell)
7. and finally... ``$  ./configure && make && sudo make install``

`VCS`_:

1. find the website
2. find clone link
3. clone the repository
4. navigate to the cloned directory (using the shell)
5. and finally... ``$  ./configure && make && sudo make install``

So, that's 2 extra steps for going the tarball way.

[**sidenote**] Other issues (specialised build systems, risks, ...)
are beyond the scope of this blog post.

.. _VCS: http://en.wikipedia.org/wiki/Revision_control
