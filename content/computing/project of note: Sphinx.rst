project of note: Sphinx
=======================

:date: 2013-02-10
:tags: project-of-note, Python



`Sphinx`_ is a tool that is used to generate documentation from
`reStructuredText`_ markup language, and is mainly used in the Python
ecosystem. I honor it much for it is a really powerful system, and I
have come to appreciate it a lot recently, with my work on documentation
of software that falls under the Pylons project.

It is a pity that the markup is not as simple as the more popular
`Markdown`_, but maybe that was out of necessity, since it is far more
advanced: it was initially built as a replacement for the tools that
build CPython documentation, which is quite extensive and needs lots of
rails.

--------------

As an example of that power, have a look at `these changes I made`_ for
`pyramid_tutorials`_. In that commit, the feature I used allows you to
include code snippets directly from files, instead of doing the
copy-paste dance, avoiding duplication and rot. This feature is known as
`literalinclude`_.

Another feature I recently worked is `intersphinx_mapping`_. What it
does it allow one to generate references in reST as if those reference
were local. For example, if you wanted to generate to CPython ``open()``
built-in function, you would need only specify it as ``:func:open``.
This is as opposed to finding the actual link and specifying it
normally.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://en.wikipedia.org/wiki/ReStructuredText
.. _Markdown: http://en.wikipedia.org/wiki/Markdown
.. _these changes I made: https://github.com/Pylons/pyramid_tutorials/commit/134190
.. _pyramid_tutorials: http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
.. _literalinclude: http://sphinx-doc.org/markup/code.html#directive-literalinclude
.. _intersphinx_mapping: http://sphinx-doc.org/ext/intersphinx.html#confval-intersphinx_mapping
