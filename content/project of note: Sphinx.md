+++
date = 2013-08-08
title = "project of note: Sphinx"
[taxonomies]
tags = ['project-of-note', 'Python', 'Pyramid']
+++

[Sphinx] is a tool that is used to generate documentation from
[reStructuredText] (rST) markup language, and is mainly used in the
Python ecosystem. I honor it much for it is a really powerful system,
and I have come to appreciate it a lot recently, with my work on
documentation of software that falls under the Pylons project.

It is a pity that the markup is not as simple as that of the more
popular [Markdown], but maybe that was out of necessity, since it is far
more advanced: it was initially built as a replacement for the tools
that build CPython documentation, which is quite extensive and needs
lots of rails.

As an example of that power, have a look at [these changes I made] for
[pyramid_tutorials]. In that commit, the feature I used allows you to
include code snippets directly from files, instead of doing the
copy-paste dance, avoiding duplication and rot. This feature is known as
[literalinclude].

Another feature I recently worked with in the recent past is
[intersphinx_mapping]. It allows one to generate references in rST as
if those reference were local. For example, if you wanted to generate a
link to the CPython `open()` built-in function, you would need only
specify it as `:func:open`. This is as opposed to finding the actual
link and specifying it normally.

One other feature I discovered (but haven't used yet) is [Info field
lists] feature. To see it in action, visit [this link], and then look at
[its markup]. It's gorgeous!

  [Sphinx]: http://sphinx-doc.org
  [reStructuredText]: http://en.wikipedia.org/wiki/ReStructuredText
  [Markdown]: http://en.wikipedia.org/wiki/Markdown
  [these changes I made]: https://github.com/Pylons/pyramid_tutorials/commit/134190
  [pyramid_tutorials]: http://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
  [literalinclude]: http://sphinx-doc.org/markup/code.html#directive-literalinclude
  [intersphinx_mapping]: http://sphinx-doc.org/ext/intersphinx.html#confval-intersphinx_mapping
  [Info field lists]: http://sphinx-doc.org/domains.html#info-field-lists
  [this link]: https://postgres-py.readthedocs.org/en/latest/#postgres.Postgres.run
  [its markup]: https://postgres-py.readthedocs.org/en/latest/_modules/postgres.html#Postgres.run
