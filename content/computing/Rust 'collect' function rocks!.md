+++
date = 2015-03-20
tags = ['Rust']
title = "Rust 'collect' function rocks!"
+++

Here is one way to populate a Vec with some data:

::: {.sourcecode}
rust

let mut vector = Vec::new(); for n in 0..COUNT { vector.push(n); };
:::

Alternatively, one can simply do this:

::: {.sourcecode}
rust

let vector = (0..COUNT).collect::\<Vec\<\_\>\>()
:::

The function is also about twice as fast, according to the following
benchmark:

::: {.sourcecode}
rust

\#!\[feature(test)\]

extern crate test;

static COUNT: i32 = 100;

\#\[bench\] fn collect(b: &mut test::Bencher) { b.iter(\|\| {
(0..COUNT).collect::\<Vec\<\_\>\>() }); }

\#\[bench\] fn no\_collect(b: &mut test::Bencher) { b.iter(\|\| { let
mut vector = Vec::new(); for n in (0..COUNT) { vector.push(n); }; vector
}); }
:::

Here is the output of `cargo bench`:

    test collect    ... bench:       164 ns/iter (+/- 7)
    test no_collect ... bench:       346 ns/iter (+/- 8)
