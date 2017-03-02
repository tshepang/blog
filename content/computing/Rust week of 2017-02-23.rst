Rust week of 2017-02-23
=======================

:date: 2017-03-02
:tags: Rust


I was glad to have the Python equivalent of the shlex__ crate,
which understands shell quoting,
helping in transforming command arguments into
what's suitable to send to ``process::Command::args``.
This allows one to avoid the pain experienced by naively doing the
following:

.. sourcecode:: rust

   let mut command = command.split(char::is_whitespace);
   let process::command::new(command.next().unwrap())
       .args(command.collect::<Vec<_>>)
       .spawn()
       ...

If the command is something like
``hg commit --message 'git eat world'``,
then the iterator would expand to:

- hg
- commit
- --message
- 'git
- eat
- world'

That will not run, and will fail with a not-obvious error message.
Using shlex, instead:

.. sourcecode:: rust

   let mut command = shlex::split(args).unwrap());
   let process::command::new(command.remove(1).unwrap())
       .args(command)
       .spawn()
       ...

Output should then be like:

- hg
- commit
- --message
- git eat world

----

`Just one contribution`__ this week,
and it's not even that great... not sure it's an improvement


__ https://crates.io/crates/shlex
__ https://github.com/ctz/hyper-rustls/pull/5
