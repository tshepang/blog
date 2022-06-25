+++
title = "Rust 2.0 wishlist"
date = 2022-06-25

[taxonomies]
tags = ['Rust']
+++

There is a strong commitment for Rust not to break backwards compatibility,
meaning that all code that compiled with Rust v1.0 should compile with all
future Rust versions, all but for exceptional circumstances.
The effort is commendable, and results in kool things like [Editions],
but mistakes/cruft/poor choices are bound to happen that cannot be fixed with such.
That is, I wish we will have a breaking release at some point,
and the pain of such a breaking change could be relieved/eliminated with
planning and migration tooling.

That said,
following are my favorite breaking things I want in Rust.

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

- Remove per-type methods where trait impls offer same functionality,
  for generality

  ```rust
  // remove
  PathBuf::as_path
  // ... in favor of
  PathBuf::as_ref

  // remove
  Path::to_path_buf
  // ... in favor of
  Path::to_owned
  ```

- Remove all deprecated APIs, most notable being the `try!` macro

### cargo

- Do not allow crate names with underscores, because taste...

  `serde_json` (bad)

  `serde-json` (good)


[more issues]: https://github.com/rust-lang/rust/pull/42397#issuecomment-315867774
[Editions]: https://doc.rust-lang.org/edition-guide/editions
