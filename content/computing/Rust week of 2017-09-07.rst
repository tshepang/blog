Rust week of 2017-09-07
=======================

:date: 2017-09-14
:tags: Rust



I had the fortune of building a Rust project at work,
and following are the libraries I used:

- I used termion__ just to clear the screen.
  API looks kool, and I plan to use it for other stuff,
  like text (and password) input.

- systemstat__ has an ugly API,
  and relies on bytesize__ for system memory data,
  whose API is not obvious,
  and has `a rather ugly display bug`__

- interfaces__ has an okay API,
  but the `get_all`__ method simply does not belong to a type named Interface.


__ https://github.com/ticki/termion
__ https://github.com/myfreeweb/systemstat
__ https://github.com/flang-project/bytesize
__ https://github.com/flang-project/bytesize/issues/8
__ https://github.com/andrew-d/interfaces-rs
__ https://docs.rs/interfaces/0.0.2/interfaces/struct.Interface.html#method.get_all
