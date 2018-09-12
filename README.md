flow pre-requisite:

- [install Rust toolchain]

- install post, a helper for creating new blog posts:

      cargo install --git https://github.com/tshepang/post

- get themes

      cd ~/blog
      git clone --recursive https://github.com/Keats/gutenberg-themes themes

flow:

- post some-title --tags some-tag some-other-tag

  + I'm then transported to the open post, with my favorite editor

- ./publish

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
---

The content of this repository is licensed under [CC BY-SA 3.0].

  [install Rust toolchain]: https://www.rust-lang.org/en-US/install.html
  [CC BY-SA 3.0]: http://creativecommons.org/licenses/by-sa/3.0
