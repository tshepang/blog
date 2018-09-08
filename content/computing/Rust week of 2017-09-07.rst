---
date: '2017-09-14'
tags: Rust
title: 'Rust week of 2017-09-07'
---

I had the fortune of building a Rust project at work, and following are
the libraries I used:

-   I used [termion] just to clear the screen. API looks kool, and I
    plan to use it for other stuff, like text (and password) input.
-   [systemstat] has an ugly API, and relies on [bytesize] for system
    memory data, whose API is not obvious, and has [a rather ugly
    display bug]
-   [interfaces] has an okay API, but the [get\_all] method simply does
    not belong to a type named Interface.

  [termion]: https://github.com/ticki/termion
  [systemstat]: https://github.com/myfreeweb/systemstat
  [bytesize]: https://github.com/flang-project/bytesize
  [a rather ugly display bug]: https://github.com/flang-project/bytesize/issues/8
  [interfaces]: https://github.com/andrew-d/interfaces-rs
  [get\_all]: https://docs.rs/interfaces/0.0.2/interfaces/struct.Interface.html#method.get_all
