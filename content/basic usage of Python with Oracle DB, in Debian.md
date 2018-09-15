+++
date = 2011-01-27
title = "basic usage of Python with Oracle DB, in Debian"

[taxonomies]
tags = ['Python']
+++

What if you wanted to access Oracle using Python? Once you are [set up],
it's real easy. We use [cx_Oracle], the most popular Python library to
read Oracle DBs.

Let's start by simply reading the DB:

``` {.sourceCode .python}
import cx_Oracle
conn = cx_Oracle.connect("usr", "pwd", "tns")
cursor = conn.cursor()
cursor.execute("SELECT * TABLE_NAME")
for item in cursor.fetchall()[0]:
    print(item)
conn.close()
```

The [cx_Oracle] explain exactly what each of these means.

If we wanted instead to modify stuff in there, we only add one extra
line, which is `cursor.commit`, like this:

``` {.sourceCode .python}
import cx_Oracle
conn = cx_Oracle.connect("usr", "pwd", "tns")
cursor = conn.cursor()
cursor.execute("SELECT * TABLE_NAME")
cursor.commit()
conn.close()
```

For real-world code, you are of course going to add exception handling
for all this, something like this:

``` {.sourceCode .python}
import cx_Oracle
try:
    conn = cx_Oracle.connect("usr", "pwd", "tns")
    cursor = conn.cursor()
    cursor.execute("SELECT * TABLE_NAME")
    for item in cursor.fetchall()[0]:
        print(item)
    conn.close()
except Exception as e:
    print(e)
```

That exception handling is rather oversimplified though, but is good
enough for illustrative purposes. Also, note that there is no timeout
set in case of problematic/slow network access, so my code will just sit
there waiting to connect.

  [set up]: http://tshepang.net/accessing-oracle-db-using-python-in-debian
  [cx_Oracle]: http://cx-oracle.sourceforge.net/html/index.html
