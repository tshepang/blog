+++
title = "nifty Zellij"
date = 2025-06-03

[taxonomies]
tags = ["Rust"]
+++

I have been using [Zellij] for years,
and its creation was a dream fulfill,
for I was hoping for a more pleasant tmux than [tmux],
and one written in Rust.

This post is about some kool features it has,
particularly ones I only recently started using:

- You can create a throwaway window, which is floating (in the foreground):

  > __C-p w__ (press a Ctrl+p combo, then press w)

  Doing the same key sequence hide them from view.

- You can create additional floating windows, which get stacked on top of the previous ones:

  > __M-n__ (Alt+n combo)

[tmux]: https://github.com/tmux/tmux
[Zellij]: https://github.com/zellij-org/zellij
