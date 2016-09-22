Rust week of 2016-09-16
=======================

:date: 2016-09-22
:tags: Rust



I looked at bcrypt__, which helps with secure password storage. I
don't quite understand how it works, but I've seen that it prevents
brute-force attacks... there is lots of CPU usage during hashing and
verification.

I continued playing with Nickel (`started few weeks ago`__), and am
liking it more, largely due discovering a less-magical way of doing
things where you'd use functions instead of a macro named
``middleware``. I've also been playing with `nickel-jwt-session`__,
which offers such a convenient API to use for working with `JSON Web
Tokens`__. I even made `two`__ `small`__ contributions to the project.


__ https://crates.io/crates/bcrypt
__ http://tshepang.net/rust-week-of-2016-09-02
__ https://github.com/kaj/nickel-jwt-session
__ https://jwt.io
__ https://github.com/kaj/nickel-jwt-session/pull/8
__ https://github.com/kaj/nickel-jwt-session/pull/9
