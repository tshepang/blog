+++
date = 2017-07-24
title = "Rust week of 2017-07-20"
[taxonomies]
tags = ['Rust']
+++

I am surprised by the ease of changing default Rust toolchain:

    # switch to nightly
    rustup default nightly
    # switch to stable
    rustup default stable

This is more easy than remembering how to tell cargo to use to use a
non-default toolchain, though that approach is not too bad either:

    # build with nightly
    cargo +nightly build

---

I made [two][] [complaints], [as][] [well][] [as][1] [five][]
[contributions].

  [two]: https://github.com/rust-lang/book/issues/828
  [complaints]: https://github.com/rust-lang/book/issues/834
  [as]: https://github.com/brson/rust-cookbook/pull/253
  [well]: https://github.com/rust-lang/rust/pull/43409
  [1]: https://github.com/rust-lang/book/pull/827
  [five]: https://github.com/rust-lang/rust/pull/43416
  [contributions]: https://github.com/BurntSushi/walkdir/pull/75
