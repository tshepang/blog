Rust 2.0 wishlist
=================

:date: 2017-06-10
:tags: Rust


- Remove the ``try!`` macro...
  it has a better replacement in the form of the ``?`` operator.

- Remove ``std::sync::mpsc`` from stdlib,
  making it available externally...
  it does not feel general enough.
