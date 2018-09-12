+++
date = 2017-11-15
title = "Rust week of 2017-11-09"

[taxonomies]
tags = ['Rust']
+++

I\'ve done nothing regarding the previous two weeks, but this week had a
look at Elasticsearch crates, as part of an effort to do some functional
testing of the system at work. What I found was [a forest of APIs]
without a good guide, but eventually ended up with something that
queries the DB and checks if certain injected data appears. I wish there
was an easy way of doing queries without having to resort to using the
json! macro:

::: {.sourcecode}
rust

let query = json!({

:

    \"sort\": \[

    :   { \"\@timestamp\": { \"order\": \"asc\", } }

    \], \"query\": { \"bool\": { \"must\": \[ { \"term\": { \"marker\":
    \"test0\" } }, { \"range\": { \"\@timestamp\": { \"gte\":
    \"now-100s\", \"lte\": \"now\", }}}, \] } }

});
:::

The [crate that allows such typed queries] happens to be incomplete and
undocumented, so will ignore it for now.

  [a forest of APIs]: https://docs.rs/elastic/*/elastic
  [crate that allows such typed queries]: https://github.com/elastic-rs/elastic/tree/master/src/queries
