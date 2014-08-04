trying to understand stack memory
=================================

:date: 2014-08-04
:tags: non-Python



Python is a language that is so high level that concepts like stack
and heap memory are hidden from its users. Not so with lower-level
languages like C. Following examples are implemented in Rust, an
easier-to-use low-level language:

.. sourcecode:: rust

   fn main() {
       let a = 0i8;
       let b = 0i8;
       let c = 0i8;

       println!("{:p}", &a);
       println!("{:p}", &b);
       println!("{:p}", &c);
   }

We build and run it like this::

  $ rustc main.rs && ./main
  0x7fff0c8d16d7
  0x7fff0c8d16d6
  0x7fff0c8d16d5

In our code, the three variables are each given 1 byte of memory
(``i8`` means 8-bit integer). The addresses are given in reverse
order. An explanation I heard is so that the heap grows the opposite
direction to the stack, which helps separate things nicely. I suppose
this would be for performance reasons and/or simpler memory management
code.

If we use large types, we'll see each value taking more than just one
address:

.. sourcecode:: rust

   fn main() {
       let a = 0i16;
       let b = 0i16;
       let c = 0i16;

       println!("{:p}", &a);
       println!("{:p}", &b);
       println!("{:p}", &c);
   }

Output::

  $ rustc main.rs && ./main
  0x7fff2462aed6
  0x7fff2462aed4
  0x7fff2462aed2

In this case, each of the variables take 2 addresses (``i16`` means
16-bit integer). Using ``i32`` results in each taking 4 addresses::

  $ rustc main.rs && ./main
  0x7ffff7706024
  0x7ffff7706020
  0x7ffff770601c

And then, finally, ``i64`` results in each variable taking 8 addresses
(64 bits) of space::

  $ rustc main.rs && ./main
  0x7fffd27383b0
  0x7fffd27383a8
  0x7fffd27383a0
