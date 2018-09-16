+++
date = 2016-08-01
title = "Rust week of 2016-08-26"
[taxonomies]
tags = ['Rust']
+++

I did learn how to use a TCP socket to communicate between 2 processes.
I found the API quite pleasing:

::: {.sourcecode}
rust

let listener = TcpListener::bind("localhost:80")? for stream in
listener.incoming() { let content = Vec::new();
stream?.read_to_end(&mut content); // do stuff with content }
:::

I also submitted [a change] that makes the example in the docs more
simple.

  [a change]: https://github.com/rust-lang/rust/pull/36134
