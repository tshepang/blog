+++
date = 2017-03-02
title = "Rust week of 2017-02-23"
[taxonomies]
tags = ['Rust']
+++

I was glad to have the Python equivalent of the [shlex] crate, which
understands shell quoting, helping in transforming command arguments
into what's suitable to send to `process::Command::args`. This allows
one to avoid the pain experienced by naively doing the following:

```rust
let mut command = command.split(char::is_whitespace);
process::command::new(command.next().unwrap())
    .args(command.collect::<Vec<_>>)
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
shlex, instead:

```rust
let mut command = shlex::split(args).unwrap());
process::command::new(command.remove(1).unwrap())
    .args(command)
    .spawn()
    ...
```

Output should then be like:

- hg
- commit
- --message
- git eat world

---

[Just one contribution] this week, and it's not even that great... not
sure it's an improvement


[shlex]: https://crates.io/crates/shlex
[Just one contribution]: https://github.com/ctz/hyper-rustls/pull/5
