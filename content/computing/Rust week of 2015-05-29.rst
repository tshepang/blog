Rust week of 2015-05-31
=======================

:date: 2015-05-30
:tags: Rust



- I was surprised by the somewhat magical Rust type inference:

  .. sourcecode:: rust

     fn main() {
         let string = "10";

         let num = match string.parse() {
             Ok(num) => num,
             Err(_) => 0,
         };

         assert_eq!(num, 10);
     }

  A more explicit call ``parse`` call would be
  ``string.parse::<i32>()``, but the type to be parsed into is
  inferred by the ``0`` that is returned in the ``Err(_)`` arm of the
  match, which is an i32. This is some far-reaching shit!

- I submitted `changes`__ to improve some of ``str`` documentaton.
  I also submitted__ a__ whole__ bunch__ of__ smaller__  changes__,


__ https://github.com/rust-lang/rust/pull/25912

__ https://github.com/rust-lang/rust/pull/25876
__ https://github.com/rust-lang/rust/pull/25907
__ https://github.com/rust-lang/rust/pull/25920
__ https://github.com/rust-lang/rust/pull/25922
__ https://github.com/rust-lang/rust/pull/25923
__ https://github.com/rust-lang/rust/pull/25936
__ https://github.com/rust-lang/rust/pull/25948
