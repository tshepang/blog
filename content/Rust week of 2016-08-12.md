+++
date = 2016-08-18
title = "Rust week of 2016-08-12"

[taxonomies]
tags = ['Rust']
+++

I enjoyed a useful (and tiny) library that helps align text nicely.
Following is an example of its usage:

::: {.sourcecode}
rust

extern crate unindent; use unindent::unindent;

fn main() {

:

    let text = \"

    :   A long text is beginning here and not in the previous line,
        because it wouldn\'t fit in comfort.

    \" println!(\"{}\", unindent(text));

}
:::

I submitted to [small][] [improvements] to its documentation. I also
contributed [a style improvement] to Cargo, the Rust package manager.

  [small]: https://github.com/dtolnay/indoc/pull/4
  [improvements]: https://github.com/dtolnay/indoc/pull/5
  [a style improvement]: https://github.com/rust-lang/cargo/pull/3015
