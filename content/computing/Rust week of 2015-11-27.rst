---
date: '2015-12-03'
tags: Rust
title: 'Rust week of 2015-11-27'
---

I added [missing][] [examples] to stdlib documentation. I also learned a
bit about [Chrono], seemingly the most comprehensive date and time
library for Rust. I used to determine what the next release date for
Rust is, using the following code:

::: {.sourcecode}
rust

extern crate chrono;

use chrono::{NaiveDate, Duration, Local};

fn main() {

:   

    for n in 0.. {

    :   // Rust 1.0 release let initial = NaiveDate::from\_ymd(2015, 5,
        15); // 1.0 was released on a Friday, but nowadays they happen
        Thursdays let release\_date =
        initial.checked\_add(Duration::weeks(6 \* n)).unwrap() -
        Duration::days(1); if release\_date \>
        Local::today().naive\_local() { println!(\"{}\", release\_date);
        break; }

    }

}
:::

  [missing]: https://github.com/rust-lang/rust/pull/30188
  [examples]: https://github.com/rust-lang/rust/pull/30190
  [Chrono]: https://github.com/lifthrasiir/rust-chrono
