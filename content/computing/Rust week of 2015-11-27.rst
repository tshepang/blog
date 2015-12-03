Rust week of 2015-11-27
=======================

:date: 2015-12-03
:tags: Rust


I added missing__ examples__ to stdlib documentation.
I also learned a bit about Chrono__, seemingly the most comprehensive
date and time library for Rust. I used to determine what the next
release date for Rust is, using the following code::

  extern crate chrono;

  use chrono::{NaiveDate, Duration, Local};

  fn main() {
      for n in 0.. {
          let d = NaiveDate::from_ymd(2015, 5, 15);  # Rust 1.0 release
          # 1.0 was released on a Friday, but nowadays they happen Thursdays
          let release_date = d.checked_add(Duration::weeks(6 * n)).unwrap() - Duration::days(1);
          if release_date > Local::today().naive_local() {
              println!("{}", release_date);
              break;
          }
      }
   }


__ https://github.com/rust-lang/rust/pull/30188
__ https://github.com/rust-lang/rust/pull/30190
__ https://github.com/lifthrasiir/rust-chrono
