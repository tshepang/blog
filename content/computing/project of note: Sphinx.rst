project of note: Sphinx
=======================

:date: 2013-08-08
:tags: project-of-note, Python, Pyramid



Sphinx__ is a tool that is used to generate documentation from
reStructuredText__ (rST) markup language, and is mainly used in the Python
ecosystem. I honor it much for it is a really powerful system, and I
have come to appreciate it a lot recently, with my work on documentation
of software that falls under the Pylons project.

It is a pity that the markup is not as simple as that of the more
popular Markdown__, but maybe that was out of necessity, since it is
far more advanced: it was initially built as a replacement for the
tools that build CPython documentation, which is quite extensive and
needs lots of rails.

--------------

As an example of that power, have a look at `these changes I made`__ for
pyramid_tutorials__. In that commit, the feature I used allows you to
include code snippets directly from files, instead of doing the
copy-paste dance, avoiding duplication and rot. This feature is known as
literalinclude__.

Another feature I recently worked with in the recent past is
`intersphinx_mapping`__. It allows one to generate
references in rST as if those reference were local. For example, if
you wanted to generate a link to the CPython ``open()`` built-in
function, you would need only specify it as ``:func:open``.  This is
as opposed to finding the actual link and specifying it normally.

One other feature I discovered (but haven't used yet) is `Info field
lists`__ feature. To see it in action, visit `this link`__, and then
look at `its markup`__. It's gorgeous!


__ http://sphinx-doc.org
__ http://en.wikipedia.org/wiki/ReStructuredText
__ http://en.wikipedia.org/wiki/Markdown
__ https://github.com/Pylons/pyramid_tutorials/commit/134190
__ http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
__ http://sphinx-doc.org/markup/code.html#directive-literalinclude
__ http://sphinx-doc.org/ext/intersphinx.html#confval-intersphinx_mapping
__ http://sphinx-doc.org/domains.html#info-field-lists
__ https://postgres-py.readthedocs.org/en/latest/#postgres.Postgres.run
__ https://postgres-py.readthedocs.org/en/latest/_modules/postgres.html#Postgres.run
