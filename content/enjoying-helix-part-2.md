+++
title = "enjoying Helix (part 2)"
date = 2023-02-18

[taxonomies]
tags = ["Rust"]
+++

_(update: there is [a part 3])_

It has been [over 2 months] since I started using Helix heavily,
and it continues to impress:

- One feature I enjoy a lot is its directory view feature,
  which you access with `:open` command.
  It displays all files in the whole directory tree,
  and allows filtering them by just typing any matching character(s),
  to the point of even doing [things like exact matching],
  in addition to fuzzy matching (the default).

- Another I love is the __jumplist__,
  which allows moving forward (`C-i`) and backward (`C-o`) through the motions that occured.
  It's extra kool in that this spans not just the current buffer,
  but others as well,
  allowing easy navigation between buffer locations reached with __Go to definition__ (`g d`).
  Emacs has a similar feature, except via twisted finger gymnastics.

I do, however, have some unfulfilled desires:

- None of [the issues I had back then][over 2 months] have been fixed.

- I wish there was [automatic saving of yanks],
  a feature available by default on Emacs
  (where older yanks are accessed with `Alt-y`, as contrasted with `C-y` for latest yanked text).
  Currently, one has to do the more awkward usage of so-called _registers_,
  which have to predefined in advance before an action (like __yank__, __delete__, or __change__).

- I have installed the editor a few times,
  and it's still not clear how things fit together...
  I have struggled too much to setup nice things like syntax highlighting and code completion.

- Too many of the themes are immature, such that I still haven't found one I could settle on.

[over 2 months]: @/enjoying-helix.md
[things like exact matching]: https://github.com/helix-editor/helix/pull/5114
[automatic saving of yanks]: https://github.com/helix-editor/helix/issues/5783
[a part 3]: @/enjoying-helix-part-3.md
