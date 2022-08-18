+++
title = "most used Rust software"
date = 2022-08-18

[taxonomies]
tags = ["Rust"]
+++

*This is in the sense of largest number of end users*

- [millions use TiKV](https://www.cncf.io/blog/2019/05/21/toc-votes-to-move-tikv-into-cncf-incubator)
  ([adopters](https://tikv.org/adopters)), a distributed transactional key-value database.

  Here are some numbers for some of those adopters:
   - [over 200m users] (late 2020)
   - [over 220m users] (mid 2019)
   - [over 300m users] (mid 2019)
   - [over 500m users] (late 2018)

  This is, for me, the most impressive Rust success story.

- [600m people use Dropbox][dropbox] (late 2019),
  [whose file storage system is written in Rust][rust@dropbox].

- [over 190m people use Firefox](https://data.firefox.com/dashboard/user-activity)
  (mid 2022), which has various components written in Rust,
  most notably Stylo, which does CSS style calculation.

- [250m people use Discord](https://discord.com/blog/why-discord-is-switching-from-go-to-rust)
  (early 2020), which has Read States service written in Rust,
  whose "sole purpose is to keep track of which channels and messages you have read".

- [100s of millions use Android 11+],
  whose DNS-over-HTTP/3 service is written in Rust.

[dropbox]: https://investors.dropbox.com/news-releases/news-release-details/dropbox-announces-fourth-quarter-and-fiscal-2019-results
[rust@dropbox]: https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire
[over 500m users]: https://en.pingcap.com/case-study/scale-out-database-powers-china-letgo-with-reduced-maintenance-costs
[over 200m users]: https://en.pingcap.com/case-study/how-chinas-insurance-giant-improved-agile-application-performance-with-a-newsql-database
[over 220m users]: https://en.pingcap.com/case-study/lesson-learned-from-queries-over-1-3-trillion-rows-of-data-within-milliseconds-of-response-time-at-zhihu
[over 300m users]: https://en.pingcap.com/case-study/how-we-use-a-scale-out-htap-database-for-real-time-analytics-and-complex-queries
[100s of millions use Android 11+]: https://twitter.com/larsberg_/status/1549722736196521987
