+++
title = "rustc compile times"
date = 2020-05-20

[taxonomies]
tags = ["Rust"]
+++

Running `./x.py build --stage 1` on a codebase that already has LLVM
built results in the following as the last line:

> Build completed successfully in 0:33:47

Following is my *config.toml*:

```toml
[build]
compiler-docs = true
extended = true
tools = [ "clippy" ]

[rust]
incremental = true
```

Following is output of latest commit:

```
❯ git show
commit 8858a435f3eef655df3e4fb6bec15d33e44a374e (HEAD -> master, origin/master, origin/HEAD)
Merge: f182c4af8a2 2d4d0dbaa72
Author: bors <bors@rust-lang.org>
Date:   Wed May 20 15:55:59 2020 +0000

    Auto merge of #72384 - mati865:ci-fix, r=pietroalbini

    Workaround MSYS2/chocolatey issue again
```
