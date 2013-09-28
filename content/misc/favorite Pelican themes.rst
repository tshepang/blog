favorite Pelican themes
=======================

:date: 2013-03-17
:tags: blogging



I don't like the default `Pelican`_ theme, ``notmyidea``:

* It is decent, but the post metadata feels cramped where its placed.
* The is no visible link to tags, never-mind a tag cloud (which is handy).
* I just don't like the general look.

So, I had a look at the others:

monospace_
----------

- [**win**] simple and elegant design
- [**win**] displays pages as a list, all but the newest one in the view
- [**win**] me loving the Archives view
- Categories are not shown in a prominent place (e.g. menu bar)
- no Tags on individual Posts
- no Categories on individual Posts
- ignores Twitter setting
- Post titles are capitalised (minor issue)


`Just Read`_
------------

- [**win**] elegant and simple design (**my favorite of all**)
- [**win**] displays pages as a list, all but the newest one in the view
- Categories are 2nd-class citizens: they aren't shown on the index page
- bullets are done wrong: the bullet-ed text is not indented
- on post view, there is no distinction between Tags and Categories
- too much border space on code snippets (**pre** tag?)
- background for code snippets is not distinctive


`tuxlite_tbs`_
--------------

- [**win**] clean and simple design: nice menu-bar and sidebars
- tags aren't shown along-aside posts


`Mockingbird`_
--------------

- [**win**] very nice and clean design
- date on Archives looks like shit
- background for code snippets is not distinctive
- Categories only visible on individual Posts
- ignores Twitter setting
- does not support Disqus


`neat`_
-------

- [**win**] the look is different; it feels calm
- Archives view is not ideal, though it's not in a prominent location
- Categories are not shown in a prominent place (e.g. on menu bar)
- when `custom fields
  <https://github.com/byk/pelican-neat#configuration-options>`_ are
  not specified, they are handled in a naive manner:

  .. image:: images/neat.png


`Chunk`_
--------

- [**win**] a trendy look
- oversized text, especially blog title
- background for code snippets is not distinctive
- Archives look like shit
- ignores Twitter setting


`Bootstrap 2`_
--------------

- [**win**] the Menu bar is unbeatable

- the general look is too busy:

  + the Categories and Tags on the right must go
  + who wants snippets on posts
  + showing Category and Tag on main views

- separate tag cloud page missing
- line length too long

.. _Mockingbird: https://github.com/wrl/pelican-mockingbird
.. _neat: https://github.com/byk/pelican-neat
.. _Bootstrap 2: https://github.com/getpelican/pelican-themes/tree/master/bootstrap2
.. _Pelican: http://docs.getpelican.com/en/latest/
.. _Just Read: https://github.com/getpelican/pelican-themes/tree/master/Just-Read
.. _tuxlite_tbs: https://github.com/getpelican/pelican-themes/tree/master/tuxlite_tbs
.. _Chunk: https://github.com/tbunnyman/pelican-chunk
.. _monospace: https://github.com/getpelican/pelican-themes/tree/master/monospace
