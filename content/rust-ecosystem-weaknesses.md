+++
title = "Rust ecosystem weaknesses"
date = 2022-08-04

[taxonomies]
tags = ["Rust"]
+++

These are problems Rust face that have nothing to do with its
capabilities as a tool,
but rather more requiring work on libraries, tooling, and advocacy:

- iOS: Rust is not tier 1 on this major platform
  (installations number the 100s of millions),
  which would help it be an alternative to Swift (and Objective-C)
- Android: Rust is not tier 1 on this major platform
  (installations number the billions),
  which would help it be an alternative to Kotlin and Java
  ([discussion])
- regulated industries, like safety critical systems:
  the compiler is not certified, leaving C and Ada as the only allowed languages
  ([example initiative])

[example initiative]: https://ferrous-systems.com/blog/ferrocene-language-specification
[discussion]: https://github.com/android/ndk/issues/1742
