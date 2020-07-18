+++
date = 2011-01-28
title = "basic ConfigParser usage"
[taxonomies]
tags = ['Python']
+++

Reading `.INI` files is very easy with Python. Say you had a file,
"*config.cfg*", with this content:

    [numbers]
    one: 1
    two: 2

The code to read that content is:

``` {.sourceCode .python}
import configparser
conf = configparser.ConfigParser()
conf.read("config.cfg")
items = conf.items("numbers")
print(items)
```

Output:

    [('one', '1'), ('two', '2')]

That's a list of tuples, each tuple a key-value pair.

Even better, since these are key-value pairs, why not use a more
suitable data type? Here goes:

``` {.sourceCode .python}
import configparser
conf = configparser.ConfigParser()
conf.read("config.cfg")
items = dict(conf.items("numbers"))
print(items)
```

Output:

    {'two': '2', 'one': '1'}

That's the **dict** function, which takes a list of tuples, and
converts them to a dictionary. You might also have noticed that the
ordering is now a bit off. That's because the dict type doesn't care
about ordering. Remember that in order to access dictionary content, you
use a key and not an index:

``` {.sourceCode .python}
>>> d = {1: 'one'}
>>> d[0]
Traceback (most recent call last):
  File "", line 1, in
KeyError: 0
>>> d[1]
'one'
```

further reading
===============

-   [configparser module]
-   [dict mapping type]

  [configparser module]: http://docs.python.org/library/configparser
  [dict mapping type]: http://docs.python.org/library/stdtypes#mapping-types-dict
