+++
title = "rustc compile times"
date = 2020-05-18

[taxonomies]
tags = ["Rust"]
+++

Running `./x.py build --stage 1` on a codebase that already has LLVM
built results in the following as the last line:

> Build completed successfully in 0:33:06

Following is my *config.toml*:

```toml
[build]
compiler-docs = true
extended = true
tools = [ "clippy" ]

[rust]
incremental = true
```
