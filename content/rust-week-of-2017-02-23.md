+++
title = "Rust week of 2017-02-23"
date = 2017-03-02

[taxonomies]
tags = ['Rust']
+++

I was glad to have the Python equivalent of the [shlex] crate, which
understands shell quoting, helping in transforming command arguments
into what's suitable to send to `process::Command::args`. This allows
one to avoid the pain experienced by naively doing the following:

```rust
let mut command = command.split(char::is_whitespace);
std::process::Command::new(command.next().unwrap())
    .args(command)
    .spawn()
...
```

If the command is something like `hg commit --message 'git eat world'`,
then the iterator would expand to:

- hg
- commit
- --message
- 'git
- eat
- world'

That will not run, and will fail with a not-obvious error message. Using
shlex, we instead:

```rust
let mut command = shlex::split(command).unwrap());
std::process::Command::new(command.remove(0).unwrap())
    .args(command)
    .spawn()
 ...
```

Output should then be like:

- hg
- commit
- --message
- git eat world


[shlex]: https://crates.io/crates/shlex
