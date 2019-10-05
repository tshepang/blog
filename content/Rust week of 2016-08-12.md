+++
date = 2016-08-18
title = "Rust week of 2016-08-12"
[taxonomies]
tags = ['Rust']
+++

I enjoyed a useful (and tiny) library that helps align text nicely.
Following is an example of its usage:

```rust
extern crate unindent;
use unindent::unindent;

fn main() {
    let text = "
        A long text is beginning here and not in the previous line,
        because it wouldn't fit in comfort.
    ";
    println!("{}", unindent(text));
}
```
