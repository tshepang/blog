various Rust ways of displaying stuff to the screen
===================================================

:date: 2015-05-25
:tags: Rust



Here is a simple way of doing it:

.. sourcecode:: rust

  use std::io::{self, Write};

  fn main() {
      io::stdout().write_all(b"some output\n");
  }

I do however get this warning when I build it::

  $ rustc main.rs
  main.rs:4:5: 4:42 warning: unused result which must be used, #[warn(unused_must_use)] on by default
  main.rs:4     io::stdout().write_ln(b"some output");
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's kill it:

.. sourcecode:: rust

  use std::io::{self, Write};

  fn main() {
      io::stdout().write_all(b"some output").unwrap();
  }

What I did is is call ``unwrap`` which basically asks our operation
to ``panic!`` in case of some error. Think of it as a shortcut of:

.. sourcecode:: rust

  use std::io::{self, Write};

  fn main() {
      match io::stdout().write_all(b"some output\n") {
          Ok(_) => (),
          Err(_) => panic!(),
      }
  }

Some docs:

* `std::io::Writer::write_line`__
* `core::result::Result::unwrap`__
* `std::panic!`__

__ http://doc.rust-lang.org/std/io/trait.Write.html#method.write_all
__ http://doc.rust-lang.org/std/result/enum.Result.html#method.unwrap
__ http://doc.rust-lang.org/std/macro.panic!.html

----

What if we wanted to do some string formatting:

.. sourcecode:: rust

  use std::io::{self, Write};

  fn main() {
      let second_word = "output";
      let text = format!("some {}\n", second_word);
      io::stdout().write_all(text.as_bytes()).unwrap();
  }

But there is a shortcut for the code above:

.. sourcecode:: rust

  use std::io::{self, Write};

  fn main() {
      let second_word = "output";
      writeln!(&mut io::stdout(), "some {}", second_word).unwrap();
  }

There is an even shorter shortcut:

.. sourcecode:: rust

  fn main() {
      let second_word = "output";
      println!("some {}", second_word);
  }

Question to self: do we get a ``panic!`` if ``println`` gets an I/O error?

Some docs:

* `std::format!`__
* `std::writeln!`__
* `std::println!`__

__ http://doc.rust-lang.org/std/macro.format!.html
__ http://doc.rust-lang.org/std/macro.writeln!.html
__ http://doc.rust-lang.org/std/macro.println!.html

----

So, why bother with all these many ways when there's a simple
``println!``? Flexibility. One example I can think of is writing to
stderr. There is no simple macro for that (``println!`` is for
stdout). Short of implementing `our own macro`__, We'd have to do
something like the following:

.. sourcecode:: rust

  use std::io;

  fn main() {
      writeln!(&mut io::stderr(), "some output");
  }

You can test that it really goes to stderr by running it like::

  $ ./main > /dev/null
  some output

__ http://stackoverflow.com/a/27590832/321731
