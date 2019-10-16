+++
title = "Rust week of 2016-12-30"
date = 2017-01-03

[taxonomies]
tags = ['Rust']
+++

We need more quality code reviews like [this one] for ripgrep.

---

I used [reqwest] for the first time, and was made sad because using HTTP
headers is as hard as doing the same for [hyper], especially given that
this is supposed to be a more easy library:

```rust
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
```

It can imagine a more nice API:

```rust
let client = reqwest::Client::new();
let auth_bearer = reqwest::Header::Bearer::new("some token");
client.get("example.com").header(auth_bearer).send();
```

I did not think much about this, so maybe there are issues with the
desired.

[this one]: http://blog.mbrt.it/2016-12-01-ripgrep-code-review
[reqwest]: https://docs.rs/reqwest
[hyper]: https://docs.rs/hyper
