+++
date = 2010-06-09
tags = ['Python']
title = "my pet project"
+++

I\'ve been working on a personal (unofficial) project for some weeks now
at work whose goal is automated testing of the system I maintain at
work. The system involves interfacing with Oracle, and the UI I used for
that is the retarded (blocky, and ugly UI, resource hog) Oracle SQL
Developer. I couldn\'t find any real alternatives after a cursory
search, and had to live with this pain for too many months. I decided to
write something in Python to achieve the common tasks of updating and
viewing specific parts of the DB. Having succeeded, I decided to turn
the script into a test suite that would eliminate the laborious and
error-prone process of doing the testing manually, a process which,
among other things, involves tweaking xml files, and using that damned
SQL Developer! I\'m not-so-many-hours away from completing this 200+
line masterpiece of mine, and here\'s what I used:

-   Python: [3.1]
-   modules: [xml.etree.ElementTree], [configparser], [sys], [time]
-   3rd party module: [cx\_Oracle] (which prompted me to write
    [instructions] for installing and setting it up)

  [3.1]: http://docs.python.org/py3k/
  [xml.etree.ElementTree]: http://docs.python.org/py3k/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
  [configparser]: http://docs.python.org/py3k/library/configparser.html#module-configparser
  [sys]: http://docs.python.org/py3k/library/sys
  [time]: http://docs.python.org/py3k/library/time
  [cx\_Oracle]: http://cx-oracle.sourceforge.net/html/index.html
  [instructions]: http://tshepang.net/accessing-oracle-db-using-python-in-debian
