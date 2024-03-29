+++
title = "project of note: Requests"
date = 2011-12-31

[taxonomies]
tags = ['project-of-note', 'Python']
+++

Requests is a Python module that makes it real easy to deal with HTTP.
As an example, something as scary as fetching a web page that needs
authentication requires only a single line of code:

```python
requests.get("https://example.com", auth=("user", "pass"))
```

It's capable of [a lot more] of course ([tutorial]), and it's weird
that something this nice hasn't been around for ages. There is another
that is much simpler to use and more advanced than Python's standard
library named [httplib2], but it's not quite as simple/elegant:

```python
h = httplib2.Http(".cache")  // ugly
h.add_credentials("user", "pass")
resp, content = h.request("https://example.com")
```

An example for achieving the same with only the standard library is far
messier.

[a lot more]: http://docs.python-requests.org/en/latest/index.html#feature-support
[tutorial]: http://docs.python-requests.org/en/latest/user/quickstart/
[httplib2]: http://code.google.com/p/httplib2/
