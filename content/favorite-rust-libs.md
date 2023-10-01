+++
title = "favorite Rust libs"
date = 2022-12-01

[taxonomies]
tags = ["Rust"]
+++

- [clap]:
  I consider this one of the killer libs in the Rust ecosystem...
  there is good taste in terms of design,
  it is comprehensive,
  and it has a very pleasant way of using it,
  the derive API.

- [serde]:
  This one seems to get even more praise (compared to [clap]),
  and is perhaps as good as anything in other language ecosystems in its domain,
  especially with its derive API (as is the case with clap).

- [anyhow]:
  The most popular error crate in the ecosystem,
  it offers very easy error handling,
  and also comes with some nice conveniences,
  like [`bail!`], [`ensure!`], and [`Context`].

[clap]: https://github.com/clap-rs/clap
[serde]: https://github.com/serde-rs/serde
[anyhow]: https://github.com/dtolnay/anyhow
[`Context`]: https://docs.rs/anyhow/latest/anyhow/trait.Context.html
[`ensure!`]: https://docs.rs/anyhow/latest/anyhow/macro.ensure.html
[`bail!`]: https://docs.rs/anyhow/latest/anyhow/macro.bail.html
