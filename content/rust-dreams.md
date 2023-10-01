+++
title = "Rust dreams"
date = 2023-10-01

[taxonomies]
tags = ["Rust"]
+++

My ideal computing environment, for all device types (from servers to embedded):

- processors are [RISC-V]
- OS is [Theseus]
  (excluding some embedded systems where there is only a single application)
  - the next best thing is having [Redox OS] reach mainstream usage
  - the next best thing after that is having [Rust in Linux kernel],
    which would require the least effort of the options above
- [rustix] (and [Mustang] / [Eyre]) are used to help run POSIX apps
- [Cranelift] is used to generate machine code

[RISC-V]: https://riscv.org/risc-v-isa
[Theseus]: https://github.com/theseus-os/Theseus
[Redox OS]: https://www.redox-os.org
[rustix]: https://github.com/bytecodealliance/rustix
[Mustang]: https://github.com/sunfishcode/mustang
[Eyre]: https://github.com/sunfishcode/eyre
[cranelift]: https://github.com/bytecodealliance/wasmtime/tree/main/cranelift
[Rust in Linux kernel]: https://www.memorysafety.org/blog/memory-safety-in-linux-kernel
