+++
title = "rustc compile times"
date = 2020-05-29

[taxonomies]
tags = ["Rust"]
+++

Running `./x.py build --stage 1` on a codebase that already has LLVM
built results in the following as the last line:

> Build completed successfully in 0:47:06

Following is my *config.toml*:

```toml
[build]
compiler-docs = true
extended = true
tools = [ "clippy", "rustfmt" ]

[rust]
incremental = true
parallel-compiler = true
```

Following is the commit I built:

```
❯ git show
commit 96dd4690c3aa70ec312448c3f2d50e6dc6fb87df (HEAD -> master, origin/master, origin/HEAD)
Merge: 77f95a89a10 3f3e0ee4b04
Author: bors <bors@rust-lang.org>
Date:   Fri May 29 11:16:45 2020 +0000

    Auto merge of #72671 - flip1995:clippyup, r=Xanewok

    Update Clippy, RLS, and rustfmt

    r? @Dylan-DPC

    This makes Clippy test-pass again: 3089c3b

    Otherwise this includes bugfixes and a few new lints.

    Fixes #72231
    Fixes #72232
```
