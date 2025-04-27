+++
title = "playin with Radicle"
date = 2025-04-27

[taxonomies]
tags = ["untagged"]
+++

One thing I wish I discovered more early while exploring Radicle is that
the simple act of cloning a Radicle repo also automatically seeds it.
I say this because I went to documentation on creating a seed node,
and found the requirements onerous (long setup instructions and a stable public ip address),
which was somewhat discouraging.

Some kool things:

- One can open an issue on the command line (`rad issue open`),
  and needs not be online to do so.
- Similarly, one can open a PR (patch) on the command line,
  also without needing to be online.
- Issues and patches (PRs) are also stored with the rest of the Radicle repo
  (though external to Git repo).
- When working on patches,
  doing a `git push --force` is not destructive (immutable),
  in that old patch versions are still accessible.
  One can even give a patch version (revision) a description, so as to detail the change.
