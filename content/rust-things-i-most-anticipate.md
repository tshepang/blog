+++
title = "Rust things I most anticipate"
date = 2022-01-01

[taxonomies]
tags = ["Rust"]
+++

The following are in progress:

- Removing non-Rust deps from toolchain
  - Removing libc dep for Linux-based systems ([mustang] and [rustix])
  - Removing llvm dep ([cranelift])
- Adding codegen backends as alternatives to [LLVM]
   - [rustc_codegen_cranelift] (for using [cranelift] as codegen backend),
     immediate benefit being fast debug compiles ([progress])
   - [rustc_codegen_gcc], allowing Rust to run in more hardware platforms
- [sled] being a production grade database... being used in tikv would be great
- Having Rust be certified for use in safety-critical systems ([Ferrocene])
- [hyper] being used as default HTTP backend of cURL ([progress]),
  because the latter has billions of installations
- [Planned inclusion in Google Chrome],
  a browser found in billions of devices
- [Pijul], a superior alternative to Git, [reaching stability]
- [Allowing Rust usage in official Linux kernel][linux],
  though this would initially be limited to device drivers

[mustang]: https://github.com/sunfishcode/mustang
[rustix]: https://github.com/bytecodealliance/rsix
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[rustc_codegen_gcc]: https://github.com/antoyo/rustc_codegen_gcc
[rustc_codegen_cranelift]: https://github.com/bjorn3/rustc_codegen_cranelift
[progress]: https://github.com/rust-lang/rust/pull/81746
[sled]: https://github.com/spacejam/sled
[hyper]: https://github.com/hyperium/hyper
[progress]: https://github.com/curl/curl/wiki/Hyper
[Ferrocene]: https://ferrous-systems.com/ferrocene
[Planned inclusion in Google Chrome]: https://security.googleblog.com/2021/09/an-update-on-memory-safety-in-chrome.html?m=1
[Pijul]: https://pijul.org
[reaching stability]: https://pijul.org/posts/2020-11-07-towards-1.0
[linux]: https://lore.kernel.org/20211206140313.5653-1-ojeda@kernel.org
[LLVM]: https://github.com/llvm/llvm-project
