+++
title = "Rust 2.0 wishlist"
date = 2019-09-07

[taxonomies]
tags = ['Rust']
+++

### lang

- Assigning values to struct bindings should use the equal sign, not
  the colon:

  ```rust
  // now
  Shoe { size: 10, style: "sneaker" };
  // dream
  Shoe { size = 10, style = "sneaker" };
  ```

  This would be consistent with the rest of the language.

### std

- All collections types removed, except these basic ones: Vec,
  HashMap, and HashSet. Also, they would also be available from
  top-level (i.e. `std::{Vec, HashMap, HashSet}`), resulting in
  `std::collections` removal.

- Rename Vec to Array, a more clear/obvious name

- Consistent names for string-y types:

  |           | current  | wish          |
  |-----------|----------|---------------|
  | string    | str      | Str           |
  |           | String   | StrOwned      |
  | os string | OsStr    | OsStr (same)  |
  |           | OsString | OsStrOwned    |
  | fs path   | Path     | Path (same)   |
  |           | PathBuf  | PathOwned     |


  Not exactly happy with above, but much better than the current 'mess'

- Remove `std::sync::mpsc` from stdlib, making it available
  externally... it does not feel general enough. ([more issues])

- Remove the `try!` macro... it has a better replacement in the form
  of the question_mark (`?`) operator.

### cargo

- Do not allow crate names with underscores, because taste...

  `lazy_static` (bad)

  `regex-syntax` (good)


[more issues]: https://github.com/rust-lang/rust/pull/42397#issuecomment-315867774
