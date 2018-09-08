---
date: '2016-09-22'
tags: Rust
title: 'Rust week of 2016-09-16'
---

I looked at [bcrypt], which helps with secure password storage. I don\'t
quite understand how it works, but I\'ve seen that it prevents
brute-force attacks\... there is lots of CPU usage during hashing and
verification.

I continued playing with Nickel ([started few weeks ago]), and am liking
it more, largely due discovering a less-magical way of doing things
where you\'d use functions instead of a macro named `middleware`. I\'ve
also been playing with [nickel-jwt-session], which offers such a
convenient API to use for working with [JSON Web Tokens]. I even made
[two][] [small] contributions to the project.

  [bcrypt]: https://crates.io/crates/bcrypt
  [started few weeks ago]: http://tshepang.net/rust-week-of-2016-09-02
  [nickel-jwt-session]: https://github.com/kaj/nickel-jwt-session
  [JSON Web Tokens]: https://jwt.io
  [two]: https://github.com/kaj/nickel-jwt-session/pull/8
  [small]: https://github.com/kaj/nickel-jwt-session/pull/9
