+++
title = "Rust week of 2015-05-29"
date = 2015-05-30

[taxonomies]
tags = ['Rust']
+++

I was surprised by the somewhat magical Rust type inference:

```rust
fn main() {
	let string = "10";
	let num = match string.parse() {
		Ok(num) => num,
		Err(_) => 0,
	};
	assert_eq!(num, 10);
}
```

A more explicit `parse` call would be `string.parse::<i32>()`, but
the type to be parsed into is inferred by the `0` that is returned
in the `Err(_)` arm of the match, which is an i32. This is some
far-reaching shit!
