+++
date = 2015-05-25
tags = ['Rust']
title = "various Rust ways of displaying stuff to the screen"
+++

Here is a simple way of doing it:

::: {.sourcecode}
rust

use std::io::{self, Write};

fn main() {

:   io::stdout().write\_all(b\"some outputn\");

}
:::

I do however get this warning when I build it:

    $ rustc main.rs
    main.rs:4:5: 4:42 warning: unused result which must be used, #[warn(unused_must_use)] on by default
    main.rs:4     io::stdout().write_ln(b"some output");
                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let\'s kill it:

::: {.sourcecode}
rust

use std::io::{self, Write};

fn main() {

:   io::stdout().write\_all(b\"some output\").unwrap();

}
:::

What I did is is call `unwrap` which basically asks our operation to
`panic!` in case of some error. Think of it as a shortcut of:

::: {.sourcecode}
rust

use std::io::{self, Write};

fn main() {

:

    match io::stdout().write\_all(b\"some outputn\") {

    :   Ok(\_) =\> (), Err(\_) =\> panic!(),

    }

}
:::

Some docs:

-   [std::io::Writer::write\_line]
-   [core::result::Result::unwrap]
-   [std::panic!]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

What if we wanted to do some string formatting:

::: {.sourcecode}
rust

use std::io::{self, Write};

fn main() {

:   let second\_word = \"output\"; let text = format!(\"some {}n\",
    second\_word); io::stdout().write\_all(text.as\_bytes()).unwrap();

}
:::

But there is a shortcut for the code above:

::: {.sourcecode}
rust

use std::io::{self, Write};

fn main() {

:   let second\_word = \"output\"; writeln!(&mut io::stdout(), \"some
    {}\", second\_word).unwrap();

}
:::

There is an even shorter shortcut:

::: {.sourcecode}
rust

fn main() {

:   let second\_word = \"output\"; println!(\"some {}\", second\_word);

}
:::

Question to self: do we get a `panic!` if `println` gets an I/O error?

Some docs:

-   [std::format!]
-   [std::writeln!]
-   [std::println!]

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

So, why bother with all these many ways when there\'s a simple
`println!`? Flexibility. One example I can think of is writing to
stderr. There is no simple macro for that (`println!` is for stdout).
Short of implementing [our own macro], We\'d have to do something like
the following:

::: {.sourcecode}
rust

use std::io;

fn main() {

:   writeln!(&mut io::stderr(), \"some output\");

}
:::

You can test that it really goes to stderr by running it like:

    $ ./main > /dev/null
    some output

  [std::io::Writer::write\_line]: http://doc.rust-lang.org/std/io/trait.Write.html#method.write_all
  [core::result::Result::unwrap]: http://doc.rust-lang.org/std/result/enum.Result.html#method.unwrap
  [std::panic!]: http://doc.rust-lang.org/std/macro.panic!.html
  [std::format!]: http://doc.rust-lang.org/std/macro.format!.html
  [std::writeln!]: http://doc.rust-lang.org/std/macro.writeln!.html
  [std::println!]: http://doc.rust-lang.org/std/macro.println!.html
  [our own macro]: http://stackoverflow.com/a/27590832/321731
