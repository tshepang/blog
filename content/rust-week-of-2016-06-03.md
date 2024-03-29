+++
title = "Rust week of 2016-06-03"
date = 2016-06-09

[taxonomies]
tags = ['Rust']
+++

I did more Rust coding than most weeks this time around, busy with some
project at work. My favorite parts:

- I love the fact that [inotify-rs] ([first mention]) collects events
  in the background, so that when you are done with whatever task you
  were busy with, you can check if there is anything new to act upon
  (e.g. a new file was created in a watched directory). This allows
  one to do away with using threads, reducing code complexity.
- Rust error handling is so nice, and forces one to think better about
  code. As an example, when doing any I/O, you mostly want to do
  that in a separate function so that you can return a `Result` type,
  something like `Result<(), std::io::Error>`. This forces you to
  isolate just the I/O handling part from the other parts of the
  logic, where you'd maybe just want to return a `bool` type. In
  my case, I would not get any I/O error, but I would get failure from
  running an external process (see `std::process` module) where the
  exit status was not 0. That meant I/O error failure case and the
  process error case had to be handled in separate places.
- In the example I gave above, `Result<(), std::io::Error>`, this
  means that we don't care about the success return value. On the
  calling side, we have an option to use a `match` statement to handle
  the result:


  ```rust
  match foo() {
      Ok(_) => (),
      Err(error) => do_something_with(error),
  }
  ```

  There is a convenient syntax to deal with such a case, where you
  don't care about one of the values... `if let`:

  ```rust
  if let Err(error) = foo() {
      do_something_with(error)
  }
  ```

  So elegant!


[inotify-rs]: https://github.com/hannobraun/inotify-rs
[first mention]: @/rust-week-of-2015-07-31.md
