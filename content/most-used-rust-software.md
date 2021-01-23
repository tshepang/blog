+++
title = "most used Rust software"
date = 2021-01-23

[taxonomies]
tags = ["Rust"]
+++

*This is in the sense of largest number of end users*

- [millions use TiKV](https://www.cncf.io/blog/2019/05/21/toc-votes-to-move-tikv-into-cncf-incubator)
  ([adopters](https://tikv.org/adopters)), a distributed transactional key-value database.

  Here are some numbers for some of those adopters:
   - [over 500m users] (early 2021)
   - [over 200m users] (late 2020)
   - [over 220m users] (mid 2019)

  This is, for me, the most impressive Rust success story.

- [600m people use Dropbox][dropbox] (late 2019),
  [whose file storage system is written in Rust][rust@dropbox].

- [over 200m people use Firefox](https://data.firefox.com/dashboard/user-activity)
  (early 20201), which has various components written in Rust,
  most notably Stylo, which does CSS style calculation.

- [250m people use Discord](https://blog.discordapp.com/a190bbca2b1f)
  (early 2020), which has Read States service written in Rust,
  whose "sole purpose is to keep track of which channels and messages you have read".

[dropbox]: https://investors.dropbox.com/news-releases/news-release-details/dropbox-announces-fourth-quarter-and-fiscal-2019-results
[rust@dropbox]: https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire
[over 500m users]: https://pingcap.com/case-studies/no-sharding-no-etl-use-scale-out-mysql-alternative-to-store-160-tb-of-data
[over 200m users]: https://pingcap.com/case-studies/how-chinas-insurance-giant-improved-agile-application-performance-with-a-newsql-database
[over 220m users]: https://pingcap.com/case-studies/lesson-learned-from-queries-over-1.3-trillion-rows-of-data-within-milliseconds-of-response-time-at-zhihu
