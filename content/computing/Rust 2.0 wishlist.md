+++
tags = ['Rust']
title = "Rust 2.0 wishlist"
date = 2017-12-09
+++

-   Remove the `try!` macro\... it has a better replacement in the form
    of the question\_mark (`?`) operator.
-   Remove `std::sync::mpsc` from stdlib, making it available
    externally\... it does not feel general enough.
-   Assigning values to struct bindings should use the equal sign, not
    the colon:

    ::: {.sourcecode}
    rust

    // now Shoe { size: 10, style: \"sneaker\") }, // dream Shoe { size
    = 10, style = \"sneaker\" };
    :::

    This would be consistent with the rest of the language.

-   All collections types removed, except these basic ones: Vec,
    HashMap, and HashSet. Also, they would also be available from
    top-level (i.e. `std::{Vec, HashMap, HashSet}`), resulting in
    `std::collections` removal.
