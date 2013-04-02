my pet project
==============

:date: 2010-06-09
:tags: Python



I've been working on a personal (unofficial) project for some weeks now
at work whose goal is automated testing of the system I maintain at
work. The system involves interfacing with Oracle, and the UI I used for
that is the retarded (blocky, and ugly UI, resource hog) Oracle SQL
Developer. I couldn't find any real alternatives after a cursory search,
and had to live with this pain for too many months. I decided to write
something in Python to achieve the common tasks of updating and viewing
specific parts of the DB. Having succeeded, I decided to turn the script
into a test suite that would eliminate the laborious and error-prone
process of doing the testing manually, a process which, among other
things, involves tweaking xml files, and using that damned SQL
Developer! I'm not-so-many-hours away from completing this 200+ line
masterpiece of mine, and here's what I used:

-  Python: `3.1`_
-  modules: `xml.etree.ElementTree`_, `configparser`_, `sys`_, `time`_
-  3rd party module: `cx_Oracle`_ (which prompted me to write
   `instructions`_ for installing and setting it up)

.. _3.1: http://docs.python.org/py3k/
.. _xml.etree.ElementTree: http://docs.python.org/py3k/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
.. _configparser: http://docs.python.org/py3k/library/configparser.html#module-configparser
.. _sys: http://docs.python.org/py3k/library/sys
.. _time: http://docs.python.org/py3k/library/time
.. _cx_Oracle: http://cx-oracle.sourceforge.net/html/index.html
.. _instructions: http://tshepang.net/accessing-oracle-db-using-python-in-debian
