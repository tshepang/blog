+++
date = 2012-06-26
title = "sorting dictionary items by value"

[taxonomies]
tags = ['Python']
+++

Following should be self-explanatory:

``` {.sourceCode .python}
$ python
>>> numbers = dict(zero=0, one=1, two=2, three=3)
>>> numbers
{'three': 3, 'zero': 0, 'two': 2, 'one': 1}
>>> sorted(numbers)
['one', 'three', 'two', 'zero']
>>> sorted(numbers, key=numbers.get)
['zero', 'one', 'two', 'three']
```

The second-last command sorts by keys, but that's easy. Sorting by
value, as shown by the last command above, is what trips many novices,
and I had to spend too much time on the web finding how to do it, and I
still don't really understand how it works, except that it works :)
