what I like about Rust
======================

:tags: Rust



- Ambitious: the aim of being memory safe without the use of a garbage
  collector, allowing it to maintain C++ execution speeds.

- Naming conventions:

  + ``name_with_underscores`` for variable and function names

  + ``HttpRequest`` instead of ``HTTPRequest`` for type names

- Error reporting: compile errors are the best I've seen (though I've
  only really seen those of C and C++); they are even color-coded!

- 2 short keywords:

  + ``fn`` for function declarations
  + ``use``, instead of ``using`` or ``import``

- The semicolon rule: I initially found it surprising that omitting a
  semicolon after a value is shorthand for returning. I appreciate it
  now... it's quite nifty, and I in fact now find ``return``
  statements ugly.

- The ``match`` statement is kool (exhaustiveness check, no
  fall-through, and nice syntax), and makes ``if..else`` chains look
  ugly.

- Allowing a trailing comma after a list of items, which is really
  great for copy-pasting and diffs.

- Packaging conventions: the build tool, Cargo, enforces that all
  build sources (which may include documentation) are placed in `src/`
  in the root of a source distribution.

- A fast-paced and time-based release cycle: a stable release will be
  made every 6 weeks, which is truly ambitious for a programming
  language.

- Development process:

  + No one, including the Core Team, pushed to the Rust tree. Each
    person gets their changes reviewed first, and they mostly get
    approved by someone else.

  + Merging the changes to the tree is nearly always done via a continuous
    integration system which first ensures that each change passes all
    automated tests.

- Allows one to redefine variables, even with different types::

    fn main() {
        let foo = 10;
        let foo = "ten";
    }

  This is convenient.
