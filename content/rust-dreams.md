+++
title = "Rust dreams"
date = 2022-09-23

[taxonomies]
tags = ["Rust"]
+++

My ideal computing environment, for all device types (from servers to embedded):

- processors are [RISC-V]
- OS is [Theseus]
  (excluding some embedded systems where there is only a single process)
- [rustix] (and [mustang]) are used to help run POSIX apps
- [Cranelift] is used to generate machine code

[RISC-V]: https://riscv.org/risc-v-isa
[Theseus]: https://github.com/theseus-os/Theseus
[rustix]: https://github.com/bytecodealliance/rustix
[mustang]: https://github.com/sunfishcode/mustang
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
