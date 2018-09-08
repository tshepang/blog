---
date: '2015-05-30'
tags: Rust
title: 'Rust week of 2015-05-29'
---

-   I was surprised by the somewhat magical Rust type inference:

    ::: {.sourcecode}
    rust

    fn main() {

    :   let string = \"10\"; let num = match string.parse() { Ok(num)
        =\> num, Err(\_) =\> 0, }; assert\_eq!(num, 10);

    }
    :::

    A more explicit `parse` call would be `string.parse::<i32>()`, but
    the type to be parsed into is inferred by the `0` that is returned
    in the `Err(_)` arm of the match, which is an i32. This is some
    far-reaching shit!

-   I submitted [changes] to improve some of `str` documentaton. I also
    [submitted][] [a][] [whole][] [bunch][] [of][] [smaller][]
    [changes][1],

  [changes]: https://github.com/rust-lang/rust/pull/25912
  [submitted]: https://github.com/rust-lang/rust/pull/25876
  [a]: https://github.com/rust-lang/rust/pull/25907
  [whole]: https://github.com/rust-lang/rust/pull/25920
  [bunch]: https://github.com/rust-lang/rust/pull/25922
  [of]: https://github.com/rust-lang/rust/pull/25923
  [smaller]: https://github.com/rust-lang/rust/pull/25936
  [1]: https://github.com/rust-lang/rust/pull/25948
