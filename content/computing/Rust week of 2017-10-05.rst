Rust week of 2017-10-05
=======================

:date: 2017-10-13
:tags: Rust



`Continuing with the work project`__,
I replaced the interfaces__ library with `pnet`__,
a weird concoction of various network functionality in one ugly mess,
but I did it because the order of the network interfaces it presents
does not randomly change (the project is UI that presents various bits
of info about the boxes that we sell, some of which is network-related),
unlike is the case with *interfaces*.
It is also comforting that the library has more users
(one__ vs. eight__ at time of writing).


__ http://tshepang.net/rust-weeks-of-2017-09-14-to-2017-09-28
__ https://github.com/andrew-d/interfaces-rs
__ https://github.com/libpnet/libpnet
__ https://crates.io/crates/interfaces/reverse_dependencies
__ https://crates.io/crates/pnet/reverse_dependencies
