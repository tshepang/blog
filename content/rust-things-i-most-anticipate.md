+++
title = "Rust things I most anticipate"
date = 2021-09-25

[taxonomies]
tags = ["Rust"]
+++

The following are in progress:

- Removing non-Rust deps from toolchain
  - Removing libc dep for Linux ([mustang] and [rsix])
  - Removing llvm dep ([cranelift])
- Adding alternative codegen backends
   - [cranelift], immediate benefit being fast debug compiles
   - [rustc_codegen_gcc], allowing Rust to run in more hardware platforms
- [sled] being a production grade database... being used in tikv would be great
- [hyper] being used as default HTTP backend of cURL ([progress]),
  because the latter has billions of installations

[mustang]: https://github.com/sunfishcode/mustang
[rsix]: https://github.com/bytecodealliance/rsix
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[rustc_codegen_gcc]: https://github.com/antoyo/rustc_codegen_gcc
[sled]: https://github.com/spacejam/sled
[hyper]: https://github.com/hyperium/hyper
[progress]: https://github.com/curl/curl/wiki/Hyper
