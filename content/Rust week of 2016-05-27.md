+++
date = 2016-06-02
title = "Rust week of 2016-05-27"
[taxonomies]
tags = ['Rust']
+++

Being a fanboy, I found the discussion [Why aren't you using Rust at
work?] rather depressing. It's also relevant to me since I am currently
writing some internal tool at work, and wonder how far it will go before
re-writing in something *more acceptable*, like Python. To be fair,
there was also [some great praise] of the ecosystem.

---

I read the intro of [rust-postgres] and even made [a small
contribution]. I also made a [doc contribution] to stdlib.

---

I was surprised that [there is no Rust set type that preserves insertion
order].

---

Something I learned about running system commands, imagine you had a
complex command like:

    ssh some-hostname "uname --all && free --human"

Running such in Rust would be:

::: {.sourcecode}
rust

std::process::Command::new("ssh")

:   .arg("some-hostname") .arg("uname --all && free --human")
    .spawn() .expect("problem");
:::

  [Why aren't you using Rust at work?]: https://www.reddit.com/r/rust/comments/4kqhqz
  [some great praise]: https://www.reddit.com/r/rust/comments/4kqhqz//d3hx9l0
  [rust-postgres]: https://github.com/sfackler/rust-postgres/blob/master/README.md
  [a small contribution]: https://github.com/sfackler/rust-postgres/pull/186
  [doc contribution]: https://github.com/rust-lang/rust/pull/34033
  [there is no Rust set type that preserves insertion order]: http://stackoverflow.com/questions/37550208
