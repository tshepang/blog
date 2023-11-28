+++
title = "Rust things I most anticipate"
date = 2023-11-28

[taxonomies]
tags = ["Rust"]
+++

The following are in progress:

- Wide use of [typst], a more pleasant alternative to latex
- Make alternative (to [LLVM]) codegen backends available in a Rust stable toolchain:
   - [rustc_codegen_cranelift],
     which uses [cranelift] for codegen,
     is already available via `rustup` on nightly toolchains,
     and the immediate benefit is fast debug compiles ([latest update][cranelift update])
   - [rustc_codegen_gcc],
     allowing Rust to run in more hardware platforms ([latest update])
- Usage in production versions of Chromium,
  though this would only be [for external dependencies]
- Having Rust be certified for use in safety-critical systems,
  most visible example being [Ferrocene] ([latest update][ferrocense status])
- [hyper] being used as default HTTP backend of cURL ([Hyper progress
  tracker] and [cURL progress tracker]),
  because the latter has billions of installations
- Removing libc dependency for Linux-based systems ([mustang] and [rustix])
- Wide use of [Pijul], a superior alternative to Git
  ([latest update](https://pijul.org/posts/2022-01-08-beta))

[mustang]: https://github.com/sunfishcode/mustang
[rustix]: https://github.com/bytecodealliance/rsix
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[rustc_codegen_gcc]: https://github.com/rust-lang/rustc_codegen_gcc
[latest update]: https://blog.antoyo.xyz/rustc_codegen_gcc-progress-report-27
[rustc_codegen_cranelift]: https://github.com/bjorn3/rustc_codegen_cranelift
[cranelift update]: https://bjorn3.github.io/2023/10/31/progress-report-oct-2023.html
[hyper]: https://github.com/hyperium/hyper
[Hyper progress tracker]: https://github.com/orgs/hyperium/projects/2/views/1
[cURL progress tracker]: https://github.com/curl/curl/wiki/Hyper
[Ferrocene]: https://ferrous-systems.com/ferrocene
[ferrocense status]: https://ferrous-systems.com/blog/the-ferrocene-language-specification-is-here
[for external dependencies]: https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html
[Pijul]: https://pijul.org
[reaching stability]: https://pijul.org/posts/2020-11-07-towards-1.0
[LLVM]: https://github.com/llvm/llvm-project
[typst]: https://github.com/typst/typst
