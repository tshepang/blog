+++
title = "enjoying Helix"
date = 2022-12-01

[taxonomies]
tags = ["Rust"]
+++

_(update: there is [a part 2])_

I have been hoping for an alternative to Emacs:

- The complexity of configuration (my `init.el` has over 200 lines)
- The sluggish behavior, especially over SSH
- The uncomfortable hurt on my left tiny finger

I may have found one in [Helix],
though it does lack certain rather important features:

- It cannot work through SSH :(
- It cannot manage files
  (though there is [a proposal to fix this])
- It cannot open files relative to that in an open buffer
  (though there is [a proposal to fix this as well])
- It cannot remove trailing whitespace on save
  (though there is [a proposal to fix this too])

Beyond that,
I love that it integrates IDE functionality without any need for configuration.
In addition,
I enjoy how responsive it is (it feels far more snappy/lightweight than Emacs).
It also has a nifty approach,
where text that would be operated on is highlighted,
and that makes it far more approachable than vi (and relatives),
to a point where I feel it takes modal editors to more mainstream audiences.

[Helix]: https://github.com/helix-editor/helix
[a proposal to fix this]: https://github.com/helix-editor/helix/pull/2377
[a proposal to fix this as well]: https://github.com/helix-editor/helix/pull/2412
[a proposal to fix this too]: https://github.com/helix-editor/helix/pull/3674
[a part 2]: @/enjoying-helix-part-2.md
