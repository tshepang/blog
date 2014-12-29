Linux threads are not deterministic
===================================

:date: 2014-12-29
:tags: non-Python


By deterministic, I am referring to their scheduling. Here's an
example in Rust::

  use std::thread::Thread;

  fn main() {
      let thread_count = 4u;
      let (tx, rx) = channel();

      for x in range(0, thread_count) {
          let tx = tx.clone();
          Thread::spawn(move || {
              println!("t{} tx", x);
              tx.send(x);
          }).detach();
      }

      for _ in range(0, thread_count) {
          println!("rx from t{}", rx.recv());
      }
  }

What I'm doing there is create 4 child threads, from which I send messages
that are to be captured by the main thread.

I built and ran it with::

  rustc --opt-level 0 main.rs && ./main

Following is output from one sample run::

  t1 tx
  t0 tx
  t2 tx
  t3 tx
  rx from t1
  rx from t0
  rx from t3
  rx from t2

Following is what I get with another run::

  t0 tx
  t1 tx
  rx from t1
  t2 tx
  rx from t2
  t3 tx
  rx from t3
  rx from t0

If it was all deterministic (i.e. predictable), it would be::

  t0 tx
  t1 tx
  t2 tx
  t3 tx
  rx from t0
  rx from t1
  rx from t2
  rx from t3
