Rust week of 2015-05-22
=======================

:date: 2015-05-25
:tags: Rust



- I bumped onto `an oddity regarding 'pow' method`__... there is no fallback.

- I found that converting a char to a String (or &str) is `not as obvious as I hoped`__.

- I read some of ``std::path`` code which resulted in `some small changes`__.

- I re-discovered the convenience function, ``Iterator::cloned``, and
  submitted two related documentation__ improvements__.

- I added syntax highlighting to the `Rust posts on my blog`__ that
  were missing it. I also updated the code to run on modern Rust.

- I got some clarity on the concept of traits by re-reading the
  well-written post, `Abstraction without overhead: traits in
  Rust`__. For example, they can be used to add methods, even to existing
  types. Here is a demonstration:

  .. sourcecode:: rust

    trait Invert {
        fn invert(&self) -> f64;
    }

    impl Invert for i32 {
        fn invert(&self) -> f64 {
            1.0/(*self as f64)
        }
    }

    fn main() {
        let foo = 10_i32;
        assert_eq!(foo.invert(), 0.1);
    }

  Another example is that one can limit the type of arguments accepted
  by a function, though it uses something of an ugly syntax:

  .. sourcecode:: rust

    fn print_inverse<T: Invert>(foo: T) {
        println!("Inverse: {}", foo.invert());
    }

  The ``<T: Invert>`` means this function will only accept ``foo``
  that implements the ``Invert`` trait.
  You can check by calling it with an ``i32`` value, in which it will
  succeed:

  .. sourcecode:: rust

    print_inverse(10_i32);

  Output::

    Inverse: 0.1

  Any other type will fail:

  .. sourcecode:: rust

    print_inverse(10_f64);

  Output::

    the trait `Invert` is not implemented for the type `f64` [E0277]

  This allows for a feature named generics, where one can use multiple
  types for the same function. For example, that error will disappear
  if you got this:

  .. sourcecode:: rust

    impl Invert for f64 {
        fn invert(&self) -> f64 {
            1.0/(*self)
        }
    }


__ http://stackoverflow.com/q/30413090/321731
__ http://stackoverflow.com/a/28003842/321731
__ https://github.com/rust-lang/rust/pull/25736
__ https://github.com/rust-lang/rust/pull/25756
__ https://github.com/rust-lang/rust/pull/25758
__ http://tshepang.net/tags.html#rust-ref
__ http://blog.rust-lang.org/2015/05/11/traits.html
