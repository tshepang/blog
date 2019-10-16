+++
title = "Rust week of 2017-06-15"
date = 2017-06-21

[taxonomies]
tags = ['Rust']
+++

I used [structopt] for the first time, and found it reduces the pain of
CLI parsing (via [clap]). Its main shortcoming is [lack of subcommand
support], whose implementation would make it a go-to for me.

[structopt]: https://github.com/TeXitoi/structopt
[clap]: https://github.com/kbknapp/clap-rs
[lack of subcommand support]: https://github.com/TeXitoi/structopt/issues/1
