+++
title = "Rust things I most anticipate"
date = 2022-12-21

[taxonomies]
tags = ["Rust"]
+++

The following are in progress:

- Make alternatives (to [LLVM]) codegen backends easily available in
  Rust toolchain (as in via `rustup`)
   - [rustc_codegen_cranelift] (for using [cranelift] as codegen backend),
     immediate benefit being fast debug compiles ([progress][cranelift PR])
   - [rustc_codegen_gcc], allowing Rust to run in more hardware
     platforms ([latest update])
- [Planned inclusion in Google Chrome],
  a browser found in billions of devices
- [Allowing Rust usage in official Linux kernel][linux],
  though this would initially be limited to device drivers
  ([initial merge], [latest proposal])
- Having Rust be certified for use in safety-critical systems,
  most visible example being [Ferrocene] ([latest update][ferrocense status])
- [hyper] being used as default HTTP backend of cURL ([Hyper progress
  tracker] and [cURL progress tracker]),
  because the latter has billions of installations
- Removing non-Rust deps from toolchain
  - Removing libc dep for Linux-based systems ([mustang] and [rustix])
  - Removing llvm dep ([cranelift])
- Wide use of [Pijul], a superior alternative to Git
  ([latest update](https://pijul.org/posts/2022-01-08-beta))

[mustang]: https://github.com/sunfishcode/mustang
[rustix]: https://github.com/bytecodealliance/rsix
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[rustc_codegen_gcc]: https://github.com/rust-lang/rustc_codegen_gcc
[latest update]: https://blog.antoyo.xyz/rustc_codegen_gcc-progress-report-18
[rustc_codegen_cranelift]: https://github.com/bjorn3/rustc_codegen_cranelift
[cranelift PR]: https://github.com/rust-lang/rust/pull/81746
[hyper]: https://github.com/hyperium/hyper
[Hyper progress tracker]: https://github.com/orgs/hyperium/projects/2/views/1
[cURL progress tracker]: https://github.com/curl/curl/wiki/Hyper
[Ferrocene]: https://ferrous-systems.com/ferrocene
[ferrocense status]: https://ferrous-systems.com/blog/the-ferrocene-language-specification-is-here
[Planned inclusion in Google Chrome]: https://groups.google.com/a/chromium.org/g/chromium-dev/c/0z-6VJ9ZpVU
[Pijul]: https://pijul.org
[reaching stability]: https://pijul.org/posts/2020-11-07-towards-1.0
[linux]: https://www.memorysafety.org/blog/memory-safety-in-linux-kernel
[initial merge]: https://www.memorysafety.org/blog/rust-in-linux-just-the-beginning
[LLVM]: https://github.com/llvm/llvm-project
[latest proposal]: https://lore.kernel.org/lkml/20221110164152.26136-1-ojeda@kernel.org
