+++
title = "enjoying Helix (part 3)"
date = 2023-08-19

[taxonomies]
tags = ["Rust"]
+++

It has been 6 months since [my last post][part 2] on my Helix adventure,
and it remains my primary text editor.

In addition to the joys expressed in [that earlier post][part 2]:
- One positive change from my previous complaints is that I have settled on a theme,
  the gorgeous Kanagawa.
- I also used `:pipe` command,
  a wonderful workdaround for when an operation is not supported by the editor.
  In my case,
  I used it for formatting JSON output (with `:pipe jaq`).

On the negative side:
- None of [the issues I had over 8 months ago] have been fixed.
- I would still like to have [automatic saving of historical yanks].
- I would love to have [searchable Prompt history],
  because it's a pain to access it via scrolling when there is lots of it.
- And on that Prompt history topic,
  there is also no support for [Persistent command history].

[part 2]: @/enjoying-helix-part-2.md
[the issues I had over 8 months ago]: @/enjoying-helix.md
[automatic saving of historical yanks]: https://github.com/helix-editor/helix/issues/5783
[searchable Prompt history]: https://github.com/helix-editor/helix/pull/2796
[Persistent command history]: https://github.com/helix-editor/helix/issues/401
