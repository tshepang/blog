---
date: '2016-02-18'
tags: Rust
title: 'Rust week of 2016-02-12'
---

I [submitted][] [four][] [documentation][] [changes] this time. I also
enjoyed reading [Two Weeks of Rust], a blog post resulting from building
something non-trivial using the language.

In terms of learning, I\'ve always been wondering why one does not need
`mut` when reading values from an iterator via a `for loop` , but does
not when reading them using `next`:

::: {.sourcecode}
rust

let it = std::env::args() // iterator over CLI arguments for value in it
{ do\_something(value); }

// versus

let mut it = std::env::args() // iterator over CLI arguments
do\_something(it.next()); do\_something(it.next()); \...
:::

I think with the `for loop`, `it` cannot be used anymore, and that\'s
why it can get away with being immutable. I\'m not 100% yet\... this
feels like a lousy explanation.

  [submitted]: https://github.com/rust-lang/rust/pull/31762
  [four]: https://github.com/rust-lang/rust/pull/31763
  [documentation]: https://github.com/rust-lang/rust/pull/31764
  [changes]: https://github.com/rust-lang/rust/pull/31765
  [Two Weeks of Rust]: http://www.matusiak.eu/numerodix/blog/2016/1/10/two-weeks-rust/
