Rust week of 2016-06-10
=======================

:date: 2016-06-16
:tags: Rust


I was made sad by the complexity of involving STDIN when using
``std::process`` module:

.. sourcecode:: rust

   fn o_to_0() -> std::io::Result<bool> {
       let mut p = std::process::Command::new("tr")
           .arg("o")
           .arg("0")
           .stdin(std::process::Stdio::piped())
           .spawn()?;
       let input = "foo";
       if let Some(stdin) = p.stdin.as_mut() {
           stdin.write_all(input.as_bytes())?;
       }
       Ok(p.wait()?.success())
   }

I wonder if this can be more easy, in other languages and/or libraries.

----

I made two__ submissions__, and gave some commentary `on another`__.


__ https://github.com/uutils/coreutils/pull/899
__ https://github.com/rust-lang/rust/pull/34314
__ https://github.com/rust-lang/rust/pull/34114
