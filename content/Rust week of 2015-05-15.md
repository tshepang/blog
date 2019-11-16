+++
title = "Rust week of 2015-05-15"
date = 2015-05-23

[taxonomies]
tags = ['Rust']
+++

I read a high quality post titled [Rust ownership, the hard way]. I
learned quite a bit going through it, like the meaning of
`#[derive(Clone, Copy)]`, which I see a lot but never knew what it
meant. I also learned that there are 7 ways to introduce a variable
binding (taking `foo` as the name of that binding):

```rust
let foo ...
for foo in ... (for loop)
foo => ... (match block)
if let foo = ... (if block)
while let foo = ... (while loop)
fn func(foo: ... (function argument)
| foo | ... (closure argument)

[Rust ownership, the hard way]: http://chrismorgan.info/blog/rust-ownership-the-hard-way.html
