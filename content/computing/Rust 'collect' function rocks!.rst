Rust 'collect' function rocks!
==============================

:date: 2015-01-17
:tags: Rust



I wanted to populate a Vec with some data, so I did it the
following way::

  let mut vector = Vec::new();
  for n in (0 ..COUNT) {
      vector.push(n);
  };

I then later found out I can simply do this::

  let vector = (0 ..COUNT).collect::<Vec<i32>>()

The function is also about twice as fast, according to the following
benchmark::

  extern crate test;

  static COUNT: i32 = 100;

  #[bench]
  fn collect(b: &mut test::Bencher) {
      b.iter(|| {
          (0 ..COUNT).collect::<Vec<i32>>()
      });
  }

  #[bench]
  fn no_collect(b: &mut test::Bencher) {
      b.iter(|| {
          let mut vector = Vec::new();
          for n in (0 ..COUNT) {
              vector.push(n);
          };
          vector
      });
  }

Here is the output of ``cargo bench``::

  running 2 tests
  test collect    ... bench:       190 ns/iter (+/- 2)
  test no_collect ... bench:       364 ns/iter (+/- 8)

  test result: ok. 0 passed; 0 failed; 0 ignored; 2 measured
