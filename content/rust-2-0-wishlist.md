+++
title = "Rust 2.0 wishlist"
date = 2023-03-09

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
careful planning and migration tooling.

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

- Minor one, but saw something like this [suggested somewhere]...
  would be nice to make the language a little smaller by unifying syntax for
  functions and closures.

  A closure syntax looks like this:

  ```rust
  fn main() {
      let square = |number: i32| {
          number * number
      };
      println!("{}", square(4));
  }
  ```

  A function for same looks like this:

  ```rust
  fn square(number: i32) -> i32 {
      number * number
  }

  fn main() {
      println!("{}", square(4));
  }
  ````

  Imagine if you could have this instead:

  ```rust
  let square: |number: i32| -> i32 = {
      number * number
  }

  fn main() {
      println!("{}", square(4));
  }
  ```

  It is a bit more heavy on tokens
  (there is an extra `:` and there is a `=`),
  but it also means one less keyword (`fn`),
  and less syntax to learn for new users.

  As a final note on this one,
  this is what a function would look like if it returned nothing:

  ```rust
  let show_square: |number: i32| = {
      println!("{}", number * number);
  }

  fn main() {
      show_square(4);
  }
  ```

- Perhaps ridiculous,
  but what if we got rid of `struct` and `enum` keywords,
  where the structure of the types is instead inferred:

  ```rust
  // current
  struct Character {
    name: String,
    kind: Kind,
  }

  enum Kind {
    Good,
    Bad,
    Ugly(Detail),
  }

  struct Detail;

  // wish
  type Character = {
    name: String,
    kind: Kind,
  }

  type Kind = {
    Good,
    Bad,
    Ugly(Detail), // looks like a struct with an unnamed field
  }

  type Detail; // implicitly a struct
  type StructWithUnnamedFields(String, Kind);

  // and unions are a special case, so we use this new syntax...
  type SomeUnion = union {
      integer: u32,
      float: f32,
  }
  ```

  This brings the syntax close to type aliases.

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


  Not exactly happy with above, but much better than the current 'mess'.

- Remove `std::sync::mpsc` from stdlib, making it available
  externally... it does not feel general enough. ([more issues])

- Remove per-type methods where trait impls offer same functionality,
  for generality:

  current | wish
  ---     | ---
  PathBuf::as_path | PathBuf::as_ref
  Path::to_path_buf | Path::to_owned
  Vec::append | Vec::extend

- Remove all deprecated APIs, most notable being the `try!` macro

- Renames of panick methods ([inspiration])

  current | wish
    ---   | ---
  foo.unwrap | (remove)
  foo.expect("message") | foo.or_panic("message")
  foo.unwrap_ord | foo.or
  foo.unwrap_or_default | foo.or_default
  foo.unwrap_or_else | foo.or_else

 ### cargo

- Do not allow crate names with underscores, because taste...

  `serde_json` (bad)

  `serde-json` (good)


[more issues]: https://github.com/rust-lang/rust/pull/42397#issuecomment-315867774
[Editions]: https://doc.rust-lang.org/edition-guide/editions
[suggested somewhere]: https://twitter.com/brundolfsmith/status/1610431400209158144
[inspiration]: https://github.com/rust-lang/rfcs/pull/3218#issuecomment-1010084722
