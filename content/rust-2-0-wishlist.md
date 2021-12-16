+++
title = "Rust 2.0 wishlist"
date = 2021-12-16

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

- Rename `Vec` to `Array`, a more clear/obvious name.
  An alternative is `List`, but that type in Python accepts members of
  different types, which is not the case for `Vec`.

- Consistent names for string-y types:

  |           | current  | wish          |
  |-----------|----------|---------------|
  | string    | str      | Str           |
  |           | String   | StrOwned      |
  | os string | OsStr    | OsStr (same)  |
  |           | OsString | OsStrOwned    |
  | C string  | CStr     | CStr (same)   |
  |           | CString  | CStrOwned     |
  | fs path   | Path     | Path (same)   |
  |           | PathBuf  | PathOwned     |


  Not exactly happy with above, but much better than the current 'mess'

- Remove `std::sync::mpsc` from stdlib, making it available
  externally... it does not feel general enough. ([more issues])

- Remove the `try!` macro... it has a better replacement in the form
  of the question_mark (`?`) operator.

### cargo

- Do not allow crate names with underscores, because taste...

  `serde_json` (bad)

  `serde-json` (good)


[more issues]: https://github.com/rust-lang/rust/pull/42397#issuecomment-315867774
