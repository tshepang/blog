+++
date = 2016-08-01
title = "Rust week of 2016-08-26"
[taxonomies]
tags = ['Rust']
+++

I did learn how to use a TCP socket to communicate between 2 processes.
I found the API quite pleasing:

```rust
let listener = std::net::TcpListener::bind("localhost:80")?;
for stream in listener.incoming() {
    let content = Vec::new();
    stream?.read_to_end(&mut content);
    // do stuff with content
}
```
