+++
date = 2014-05-10
title = "a better Python"
[taxonomies]
tags = ['Python', 'non-Python']
+++

[This post] led me to an interesting paper titled *An Empirical
Investigation into Programming Language Syntax*. Now, since I'm a
Python sucker, here is what I would change in Python in order to follow
advice from [that paper]:

```
    before       after
    ------       -----
     !=          not=
      %          mod
   string        text
  try-except  check-error
   finally       always
    raise        alert
     def       procedure
    print       output
   import        use
  int/float     number
```

The most surprising finding is that both programmers and non-programmers
found *while* and *for* not intuitive for looping constructs. The
preferred alternatives are *repeat* and *loop*. Of these, I prefer
*loop*, but it does not read as well as *while*:

    while count < 3:
        count = action()

    loop count < 3:
        count = action()

Quorum, the language by those responsible for this paper, went with:

    repeat while (count < 3)
        count = action()
    end

To mimic that in Python, any of the following two sound fine (I prefer
*if* to *while*; less syntax is better):

    repeat if count < 3:
        count = action()

    loop if count < 3:
        count = action()

That means an infinite loop would be:

    loop if True:
        action()

Or for that special case, a shortcut can just be this simple:

    loop:
        action()

I wonder what cycling through items in a container would look like. In
Python, it looks like:

    for item in container:
        action(item)

This feels as natural as anything, but then again I been doing Python
for a number of years, so the bias could be heavy. Following is an
attempt:

    loop in range(3):
        action()

It mimics this Python syntax, which I actually don't like, since we
don't always need the items of the container:

    for _ in range(3):
        action()

Quorum, the academic language mentioned above, does it like:

    repeat 3 times
        action()
    end

I don't like that either; feels contrived. The Python way strikes me as
a good compromise, especially given how general it is. I will try again
with the *loop* syntax:

    loop item in container:
        action(item)

You have to admit it doesn't read as nice as:

    for item in container:
        action(item)

It should be flexible to accommodate more than just one value on each
iteration, so should have an equivalent for this Python code:

    for index, item in enumerate(container):
        action(index, item)

Here goes:

    loop index, item in enumerate(container):
        action(index, item)

Now, for the much-loved Python list comprehensions:

    [procedure(item) for item in container]

We would instead have:

    [procedure(item) loop item in container]

So, apart from being highly-rated for being intuitive, *loop* also
provides a consistent looping construct, whereas Python has 2, *while*
and *for*, both of which received low points in the study. Interesting.

If someone (me?) were to implement these changes to Python, the result
would not be named a Python variant (they are just too drastic), but
more a Python descendent... **a better Python**.

  [This post]: http://neverworkintheory.org/2014/01/29/stefik-siebert-syntax
  [that paper]: http://dl.acm.org/authorize?6968137
