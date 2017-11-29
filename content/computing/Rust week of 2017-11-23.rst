Rust week of 2017-11-23
=======================

:date: 2017-11-29
:tags: Rust



There wasn't much last week, other than continuing with the functional
testing work that queries Elasticsearch.
This week, however, saw me extending mrh__
(Pending is a repo state that requires action):

- Allow ignoring Untracked files in output (feature request from a friend)
- Distinguish Untracked state from other Pendings
- Add 3 more Pendings: added, removed, renamed
- Do not quit after encountering malformed repos
- Add color to output (via colored)
- Add option to display absolute paths
- Check if HEAD is tagged (with `some help from Stack Overflow`__)

I am glad.


__ https://crates.io/crates/mrh
__ https://stackoverflow.com/q/47500612/321731
