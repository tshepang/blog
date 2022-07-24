+++
title = "Rust week of 2016-02-12"
date = 2016-02-18

[taxonomies]
tags = ['Rust']
+++

I
enjoyed reading [Two Weeks of Rust], a blog post resulting from building
something non-trivial using the language.

In terms of learning, I've always been wondering why one does not need
`mut` when reading values from an iterator via a `for loop` , but does
not when reading them using `next`:

```rust
let it = std::env::args() // iterator over CLI arguments
for value in it {
    do_something(value);
}

// versus

let mut it = std::env::args() // iterator over CLI arguments
do_something(it.next());
do_something(it.next());
...
```

I think with the `for loop`, `it` cannot be used anymore, and that's
why it can get away with being immutable. I'm not 100% yet... this
feels like a lousy explanation.

[Two Weeks of Rust]: http://www.matusiak.eu/numerodix/blog/2016/1/10/two-weeks-rust/
