+++
title = "Rust things I most anticipate"
date = 2025-01-12

[taxonomies]
tags = ["Rust"]
+++

- Wide use of [Radicle],
  an alternative to GitHub that is peer-to-peer ([latest update][radicle update])
- Make alternative (to [LLVM]) codegen backends available in a Rust stable toolchain:
   - [rustc_codegen_cranelift],
     which uses [cranelift] for codegen,
     is already available via `rustup` on nightly toolchains,
     and the immediate benefit is fast debug compiles ([updates][rustc_codegen_cranelift updates])
   - [rustc_codegen_gcc],
     allowing Rust to run in more hardware platforms ([updates][rustc_codegen_gcc updates])
- More drivers written in Rust in the official Linux kernel,
  most promising ones being:
  - [Binder] (for Android IPC)
  - Apple GPU driver ([latest update][apple gpu driver update]),
    which seems to be one that has attracted the most attention
- Use of Rust in safety-critical systems,
  [Ferrocene] being the most likely candidate,
  due to being the first (and only) Rust toolchain [qualified for the domain]
- Wide use of [Typst], a more pleasant alternative to LaTeX
- Usage in production versions of Chromium,
  though this would only be [for external dependencies]
- Removing libc dependency for Linux-based systems ([mustang] and [rustix])
- Wide use of [Pijul], for I want a better VCS than Git
  ([latest update](https://pijul.org/posts/2022-01-08-beta))

### achieved

- A driver written in Rust in the official Linux kernel:
  - [Asix PHYs driver](https://github.com/torvalds/linux/blob/master/drivers/net/phy/ax88796b_rust.rs)
    is the first, released early 2024

[mustang]: https://github.com/sunfishcode/mustang
[rustix]: https://github.com/bytecodealliance/rsix
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[rustc_codegen_gcc]: https://github.com/rust-lang/rustc_codegen_gcc
[rustc_codegen_gcc updates]: https://blog.antoyo.xyz
[rustc_codegen_cranelift]: https://github.com/bjorn3/rustc_codegen_cranelift
[rustc_codegen_cranelift updates]: https://bjorn3.github.io
[Ferrocene]: https://ferrous-systems.com/ferrocene
[for external dependencies]: https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html
[Pijul]: https://pijul.org
[reaching stability]: https://pijul.org/posts/2020-11-07-towards-1.0
[LLVM]: https://github.com/llvm/llvm-project
[Typst]: https://github.com/typst/typst
[qualified for the domain]: https://ferrous-systems.com/blog/officially-qualified-ferrocene
[Binder]: https://lore.kernel.org/rust-for-linux/20231101-rust-binder-v1-0-08ba9197f637@google.com
[apple gpu driver update]: https://asahilinux.org/2023/03/road-to-vulkan
[Radicle]: https://radicle.xyz
[radicle update]: https://radicle.xyz/2024/12/05/radicle-1.1.html
