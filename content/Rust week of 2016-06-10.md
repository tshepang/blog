+++
date = 2016-06-16
title = "Rust week of 2016-06-10"

[taxonomies]
tags = ['Rust']
+++

I was made sad by the complexity of involving STDIN when using
`std::process` module:

::: {.sourcecode}
rust

fn o\_to\_0() -\> std::io::Result\<bool\> {

:

    let mut p = std::process::Command::new(\"tr\")

    :   .arg(\"o\") .arg(\"0\") .stdin(std::process::Stdio::piped())
        .spawn()?;

    let input = \"foo\"; if let Some(stdin) = p.stdin.as\_mut() {
    stdin.write\_all(input.as\_bytes())?; } Ok(p.wait()?.success())

}
:::

I wonder if this can be more easy, in other languages and/or libraries.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

I made [two][] [submissions], and gave some commentary [on another].

  [two]: https://github.com/uutils/coreutils/pull/899
  [submissions]: https://github.com/rust-lang/rust/pull/34314
  [on another]: https://github.com/rust-lang/rust/pull/34114
