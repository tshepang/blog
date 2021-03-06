+++
title = "Rust 'collect' function rocks!"
date = 2015-03-20

[taxonomies]
tags = ['Rust']
+++

Here is one way to populate a Vec with some data:

```rust
let mut vector = Vec::new();
for n in 0..COUNT {
    vector.push(n);
};
```

Alternatively, one can simply do this:

```rust
let vector = (0..COUNT).collect::<Vec<_>>()
```

The function is also about twice as fast, according to the following
benchmark:

```rust
#![feature(test)]
extern crate test;

static COUNT: i32 = 100;

#[bench]
fn collect(b: &mut test::Bencher) {
    b.iter(|| {
        (0..COUNT).collect::<Vec<_>>()
    });
}

#[bench]
fn no_collect(b: &mut test::Bencher) {
    b.iter(|| {
        let mut vector = Vec::new();
        for n in (0..COUNT) {
            vector.push(n);
        };
        vector
    });
}
```

Here is the output of `cargo bench`:

```
test collect    ... bench:       164 ns/iter (+/- 7)
test no_collect ... bench:       346 ns/iter (+/- 8)
```
