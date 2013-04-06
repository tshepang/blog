what me loves about static website generation
=============================================

:date: 2013-04-06
:tags: blogging



There's a ridiculous amount of power and flexiblity in having all the
blog sources locally:

- One can use text editor of choice, which is a big help,
  given the quality of web-based editors in general.

- What this implies is that I can now put the blog in a VCS__.
  This acts as some sort of backup too,
  since I place my sources on `a remote server`__. [#]_

- This also means that I can do a heck of a lot of edits without being
  connected to the web, or deeper changes like playing search-replace
  through the entire blog.


cons
----

* The complexity of `the setup`__ is going to scare many people away.
* It can take a lot of time to setup;
  For me, this was made worse by having a lot of posts, as well as
  `being rather particular`__ about the look and functionality of the output.


.. [#] I used to run a command like ``wget --mirror http://tshepang.net``
   once in a while, just in case!

__ http://en.wikipedia.org/wiki/Revision_control
__ https://bitbucket.org/tshepang/blog
__ http://tshepang.net/blogging-with-pelican
__ http://tshepang.net/favorite-pelican-themes
