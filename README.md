flow pre-requisite:

- [install Rust toolchain]

- install post, a helper for creating new blog posts:

      cargo install --git https://github.com/tshepang/post

- get theme

      cd ~/blog
      mkdir themes && cd themes
      git clone --recursive https://github.com/tshepang/after-dark --branch custom

flow:

- `post some-title --tags some-tag some-other-tag`

  + I'm then transported to the open post, with my favorite editor

- `./publish`

demo:

```
❯ post 'Rust ecosystem weaknesses' --tags Rust

❯ cat "~/blog/content/movies/Fight Club (1999).md"
+++
title = "Rust ecosystem weaknesses"
date = 2022-06-24

[taxonomies]
tags = ["Rust"]
+++
```

---

The content of this repository is licensed under [CC BY-SA 4.0].

[install Rust toolchain]: https://rust-lang.org/install
[CC BY-SA 4.0]: http://creativecommons.org/licenses/by-sa/4.0
