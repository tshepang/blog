+++
title = "small Rust projects I wish were worked on"
date = 2023-01-22

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
  Looking further in the future,
  Git should be discarded in favor of a [Pijul].

- Maintnenance of [sd],
  a kool sed replacement.
  It not had a release in over 2 years.

- Maintnenance of [tokei],
  a kool code stats tool that cares for accuracy.
  Like [sd], it also not had a release in over 2 years.

[git2-rs use rustls]: https://github.com/rust-lang/git2-rs/issues/623
[gitoxide]: https://github.com/Byron/gitoxide
[Pijul]: https://pijul.org
[sd]: https://github.com/chmln/sd
[tokei]: https://github.com/xampprocky/tokei
