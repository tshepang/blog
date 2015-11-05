Rust week of 2015-10-30
=======================

:date: 2015-11-06
:tags: Rust



Just `one submission`__ this time around. Yep! I did however spend
time pondering the magical forward type inference that I first
experienced `back in May`__, this time sparked by `this example`__;
see this line::

  let address = "0.0.0.0:6567".parse().unwrap();

You actually have to read further to figure the type that URL is going
to be parsed as::

  let server = TcpListener::bind(&address).unwrap();

It would be less surprising if we had the following instead::

  let address = SocketAddr::from_str("0.0.0.0:6567".unwrap();
  let server = TcpListener::bind(&address).unwrap();


__ https://github.com/rust-lang/rust/pull/29651
__ http://tshepang.net/rust-week-of-2015-05-29
__ https://github.com/carllerche/mio/blob/getting-started/doc/getting-started.md#writing-the-echo-server
