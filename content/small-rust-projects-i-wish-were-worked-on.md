+++
title = "small Rust projects I wish were worked on"
date = 2022-06-19

[taxonomies]
tags = ["Rust"]
+++

Here are some small project ideas:

- Make [git2-rs use Rustls], which would replace a dependency on OpenSSL.
  There are 2 reasons why this is appealing:
  - OpenSSL is written in C, and its code quality is not considered stellar
  - C dependencies are not as pleasant to work with as Rust ones in Cargo,
    both for users and for maintainers

[git2-rs use rustls]: https://github.com/rust-lang/git2-rs/issues/623
