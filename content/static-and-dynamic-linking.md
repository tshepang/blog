+++
title = "static and dynamic linking"
date = 2022-07-26

[taxonomies]
tags = ["Rust"]
+++

*Let us simplify the model by assuming there is an executable (exe)
and a single dependency (dep)*

For a language that lacks ABI (such as Rust),
the challenge with dynamic linking is that new versions of
a dep will require rebuilding the exe,
unless multiple versions of the dep are kept around
(which defeats the point of dynamic linking).
That flaw does not affect the exe that has static linking,
since they have all they need embedded in them.

Beyond that, dynamic linking has clear wins...

- where a change does __not__ require a new toolchain:

  | change | static linking      | dynamic linking |
  |--------|---------------------|-----------------|
  | dep    | rebuild all, relink | rebuild         |
  | exe    | rebuild, relink     | rebuild         |

- where a change requires a new toolchain:

  | change | static linking      | dynamic linking |
  |--------|---------------------|-----------------|
  | dep    | rebuild all, relink | rebuild all     |
  | exe    | rebuild all, relink | rebuild all     |

It's not an easy trade, so actual numbers would help.
Assuming there are no other problems related to dynamic linking,
there are two alternatives:

- The dep and exe is rebuilt each time a new toolchain is released,
  to benefit from possible improvements such better codegen.
- Toolchain releases do not result in any (automatic) rebuilds,
  unless there are changes in either the dep or the exe.
  This seems reasonable,
  and has no disadvantages compared to static linking.
