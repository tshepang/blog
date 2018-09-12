+++
date = 2015-05-23
tags = ['Rust']
title = "Rust week of 2015-05-15"
+++

This is the first of what I intend to be a weekly series of posts
related to my favorite programming language. I here take Rust weeks to
begin each Friday, since Stable releases of the Rust distribution
(language and included libraries) are to be released on that week day.
This is also a great excuse to write more regularly.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

-   I read a high quality post titled [Rust ownership, the hard way]. I
    learned quite a bit going through it, like the meaning of
    `#[derive(Clone, Copy)]`, which I see a lot but never knew what it
    meant. I also learned that there are 7 ways to introduce a variable
    binding (taking `foo` as the name of that binding):

        let foo ...
        for foo in ... (for loop)
        foo => ... (match block)
        if let foo = ... (if block)
        while let foo = ... (while loop)
        fn func(foo: ... (function argument)
        | foo | ... (closure argument)

-   I [submitted][] [some][] [documentation][] [improvements]. The
    latter one was especially time-consuming, but it helped me explore
    the `std::path` module. It even led me to bump onto [a rustdoc bug].

  [Rust ownership, the hard way]: http://chrismorgan.info/blog/rust-ownership-the-hard-way.html
  [submitted]: https://github.com/rust-lang/rust/pull/25629
  [some]: https://github.com/rust-lang/rust/pull/25656
  [documentation]: https://github.com/rust-lang/rust/pull/25659
  [improvements]: https://github.com/rust-lang/rust/pull/25666
  [a rustdoc bug]: https://github.com/rust-lang/rust/issues/25673