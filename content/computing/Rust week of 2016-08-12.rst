Rust week of 2016-08-12
=======================

:date: 2016-08-18
:tags: Rust


I enjoyed a useful (and tiny) library that helps align text
nicely. Following is an example of its usage:

.. sourcecode:: rust

   extern crate unindent;
   use unindent::unindent;

   fn main() {
       let text = "
           A long text is beginning here and not in the previous line,
           because it wouldn't fit in comfort.
       "
       println!("{}", unindent(text));
   }

I submitted to small__ improvements__ to its documentation. I also
contributed `a style improvement`__ to Cargo, the Rust package manager.


__ https://github.com/dtolnay/indoc/pull/4
__ https://github.com/dtolnay/indoc/pull/5
__ https://github.com/rust-lang/cargo/pull/3015
