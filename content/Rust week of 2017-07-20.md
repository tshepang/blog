+++
title = "Rust week of 2017-07-20"
date = 2017-07-24

[taxonomies]
tags = ['Rust']
+++

I am surprised by the ease of changing default Rust toolchain:

    # switch to nightly
    rustup default nightly
    # switch to stable
    rustup default stable

This is more easy than remembering how to tell cargo to use a
non-default toolchain, though that approach is not too bad either:

    # build with nightly
    cargo +nightly build
