Rust week of 2016-05-27
=======================

:date: 2016-06-02
:tags: Rust



Being a fanboy, I found the discussion `Why aren't you using Rust at
work?`__ rather depressing. It's also relevant to me since I am
currently writing some internal tool at work, and wonder how far it
will go before re-writing in something *more acceptable*, like
Python. To be fair, there was also `some great praise`__ of the ecosystem.

----

I read the intro of `rust-postgres`__ and even made `a small
contribution`__. I also made a `doc contribution`__ to stdlib.

----

I was surprised that `there is no Rust set type that preserves
insertion order`__.

----

Something I learned about running system commands, imagine you had a
complex command like::

  ssh some-hostname "uname --all && free --human"

Running such in Rust would be:

.. sourcecode:: rust

   std::process::Command::new("ssh")
      .arg("some-hostname")
      .arg("uname --all && free --human")
      .spawn()
      .expect("problem");


__ https://www.reddit.com/r/rust/comments/4kqhqz
__ https://www.reddit.com/r/rust/comments/4kqhqz//d3hx9l0
__ https://github.com/sfackler/rust-postgres/blob/master/README.md
__ https://github.com/sfackler/rust-postgres/pull/186
__ https://github.com/rust-lang/rust/pull/34033
__ http://stackoverflow.com/questions/37550208
