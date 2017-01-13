Rust week of 2016-12-30
=======================

:date: 2017-01-03
:tags: Rust



We need more quality code reviews like `this one`__ for ripgrep.

----

I used reqwest__ for the first time,
and was made sad because using HTTP headers is as hard as doing the
same for hyper__,
especially given that this is supposed to be a more easy library:

.. sourcecode:: Rust

   let mut auth_bearer = Headers::new();
   headers.set(
       Authorization (
           Bearer {
               token: "some token",
           }
       )
   );
   let mut client = reqwest::Client::new();
   client.get("example.com").headers(auth_bearer).send();

It can imagine a more nice API:

.. sourcecode:: Rust

   let client = reqwest::Client::new();
   let auth_bearer = reqwest::Header::Bearer::new("some token");
   client.get("example.com").header(auth_bearer).send();

I did not think much about this, so maybe there are issues with the desired.

----

Just `one contribution`__ this time.


__ http://blog.mbrt.it/2016-12-01-ripgrep-code-review
__ https://docs.rs/reqwest
__ https://docs.rs/hyper

__ https://github.com/serde-rs/json/pull/182
