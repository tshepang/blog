+++
title = "small Rust projects I wish were worked on"
date = 2022-12-28

[taxonomies]
tags = ["Rust"]
+++

Here are some small project ideas:

- Make [git2-rs use Rustls], which would replace a dependency on OpenSSL.
  There are 2 reasons why this is appealing:

  - OpenSSL is written in C, and its code quality is not considered stellar

  - C dependencies are not as pleasant to work with as Rust ones in Cargo,
    both for users and for maintainers

  Even better would be replacement of __git2-rs__ with [gitoxide],
  a pure Rust implementation.

[git2-rs use rustls]: https://github.com/rust-lang/git2-rs/issues/623
[gitoxide]: https://github.com/Byron/gitoxide
