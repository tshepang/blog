+++
date = 2015-07-01
title = "Rust week of 2015-06-26"

[taxonomies]
tags = ['Rust']
+++

I [removed a sentence] that is not needed from Cargo documentation. I
also added [ability to read from $EMAIL environment variable] to the
`cargo new` command, and [fixed a small issue] in the test suite..

In the Rust tree:

-   I [fixed] one oversight where someone missed removing some obsolete
    doc and annotations while they were removing obsolete code
-   I [fixed][1] some bad code indents
-   I [added] an example for reading from stdin
-   I [removed] a misleading sentence
-   I then [fixed][2] a typo

  [removed a sentence]: https://github.com/rust-lang/cargo/pull/1754
  [ability to read from $EMAIL environment variable]: https://github.com/rust-lang/cargo/pull/1755
  [fixed a small issue]: https://github.com/rust-lang/cargo/pull/1756
  [fixed]: https://github.com/rust-lang/rust/pull/26621
  [1]: https://github.com/rust-lang/rust/pull/26622
  [added]: https://github.com/rust-lang/rust/pull/26627
  [removed]: https://github.com/rust-lang/rust/pull/26724
  [2]: https://github.com/rust-lang/rust/pull/26725
