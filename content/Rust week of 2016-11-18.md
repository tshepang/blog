+++
date = 2016-11-24
title = "Rust week of 2016-11-18"

[taxonomies]
tags = ['Rust']
+++

I was surprised by the ease of use of [libflate] when decompressing a
gzip'ed file:

::: {.sourcecode}
rust

extern crate libflate;

fn main() {

:   let mut file = std::fs::<File::open>("file.gz").unwrap(); let file
    = libflate::gzip::Decoder::new(&mut file).unwrap();
    do_something_with(file);

};
:::

And that's it, `file` is now like a normal file!

Another module I used for the first time is [regex], which seems to have
such a well-designed API actually.

---

I made just [one contribution] this week.

  [libflate]: https://crates.io/crates/libflate
  [regex]: https://crates.io/crates/regex
  [one contribution]: https://github.com/rust-lang/rust/pull/37956
