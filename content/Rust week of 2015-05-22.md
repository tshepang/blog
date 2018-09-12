+++
date = 2015-05-25
title = "Rust week of 2015-05-22"

[taxonomies]
tags = ['Rust']
+++

-   I bumped onto [an oddity regarding \'pow\' method]\... there is no
    fallback.
-   I found that converting a char to a String (or &str) is [not as
    obvious as I hoped].
-   I read some of `std::path` code which resulted in [some small
    changes].
-   I re-discovered the convenience function, `Iterator::cloned`, and
    submitted two related [documentation][] [improvements].
-   I added syntax highlighting to the [Rust posts on my blog] that were
    missing it. I also updated the code to run on modern Rust.
-   I got some clarity on the concept of traits by re-reading the
    well-written post, [Abstraction without overhead: traits in Rust].
    One feature they have is they allow adding methods to types,
    including upstream ones, example being stdlib types as follows:

    ::: {.sourcecode}
    rust

    trait Invert {

    :   fn invert(&self) -\> f64;

    }

    impl Invert for i32 {

    :

        fn invert(&self) -\> f64 {

        :   1.0/(\*self as f64)

        }

    }

    fn main() {

    :   let foo = 10\_i32; assert\_eq!(foo.invert(), 0.1);

    }
    :::

    Another example is that one can limit the type of arguments accepted
    by a function, though it uses something of an ugly syntax:

    ::: {.sourcecode}
    rust

    fn print\_inverse\<T: Invert\>(foo: T) {

    :   println!(\"Inverse: {}\", foo.invert());

    }
    :::

    The `<T: Invert>` means this function will only accept `foo` whose
    type implements the `Invert` trait. You can check by calling it with
    an `i32` value, in which it will succeed:

    ::: {.sourcecode}
    rust

    print\_inverse(10\_i32);
    :::

    Output:

        Inverse: 0.1

    Any other type will fail:

    ::: {.sourcecode}
    rust

    print\_inverse(10\_f64);
    :::

    Output:

        the trait `Invert` is not implemented for the type `f64` [E0277]

    This allows for a feature named generics, where one can use multiple
    types for the same function. For example, that error will disappear
    if you got this:

    ::: {.sourcecode}
    rust

    impl Invert for f64 {

    :

        fn invert(&self) -\> f64 {

        :   1.0/(\*self)

        }

    }
    :::

  [an oddity regarding \'pow\' method]: http://stackoverflow.com/q/30413090/321731
  [not as obvious as I hoped]: http://stackoverflow.com/a/28003842/321731
  [some small changes]: https://github.com/rust-lang/rust/pull/25736
  [documentation]: https://github.com/rust-lang/rust/pull/25756
  [improvements]: https://github.com/rust-lang/rust/pull/25758
  [Rust posts on my blog]: http://tshepang.net/tags.html#rust-ref
  [Abstraction without overhead: traits in Rust]: http://blog.rust-lang.org/2015/05/11/traits.html
