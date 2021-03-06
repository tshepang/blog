flow pre-requisite:

- [install Rust toolchain]

- install post, a helper for creating new blog posts:

      cargo install --git https://github.com/tshepang/post

- get theme

      cd ~/blog
      mkdir themes && cd themes
      git clone --recursive https://github.com/tshepang/even --branch custom

flow:

- `post some-title --tags some-tag some-other-tag`

  + I'm then transported to the open post, with my favorite editor

- `./publish`

demo:
```
$ post 'Fight Club (1999)' --movies --tags 1999-movie masterpiece
$ cat "~/blog/content/movies/Fight Club (1999).md"
+++
title = "Fight Club (1999)"
date = 2018-09-12

[taxonomies]
tags = ["1999-movie", "masterpiece"]
+++
$ post 'I loved Python' --tags non-Rust
$ cat "~/blog/content/I loved Python.md"
+++
title = "I loved Python"
date = 2018-09-12

[taxonomies]
tags = ["non-Rust"]
```

wishlist:

- tags should be displayed on the page
- there should be /tags and /movies/tags

---

The content of this repository is licensed under [CC BY-SA 4.0].

[install Rust toolchain]: https://rust-lang.org/install
[CC BY-SA 4.0]: http://creativecommons.org/licenses/by-sa/4.0
