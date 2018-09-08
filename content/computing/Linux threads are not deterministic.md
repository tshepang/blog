---
date: '2015-05-25'
tags: Rust
title: Linux threads are not deterministic
---

By deterministic, I am referring to their scheduling. Here\'s an example
in Rust:

::: {.sourcecode}
rust

use std::thread; use std::sync::mpsc::channel;

fn main() {

:   let thread\_count = 4; let (tx, rx) = channel();

    for x in 0..thread\_count {

    :   let tx = tx.clone(); thread::spawn(move \|\| { println!(\"t{}
        tx\", x); tx.send(x).unwrap(); });

    }

    for \_ in 0..thread\_count {

    :   println!(\"rx from t{}\", rx.recv().unwrap());

    }

}
:::

What I\'m doing there is create 4 child threads, from which I send
messages that are to be captured by the main thread.

I built and ran it with:

    rustc --opt-level 0 main.rs && ./main

Following is output from one sample run:

    t1 tx
    t0 tx
    t2 tx
    t3 tx
    rx from t1
    rx from t0
    rx from t3
    rx from t2

Following is what I get with another run:

    t0 tx
    t1 tx
    rx from t1
    t2 tx
    rx from t2
    t3 tx
    rx from t3
    rx from t0

If it was all deterministic (i.e. predictable), `t0 tx` would always
come before `t1 tx`, and `rx from t0` before `rx from t1`, and so on.

I think this is done for performance reasons, where the kernel just
looks for an available slot, running each thread on a best-effort basis.
My guess is that a more real-time kernel would be more predictable.
