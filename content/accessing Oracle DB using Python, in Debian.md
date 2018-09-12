+++
date = 2011-01-15
title = "accessing Oracle DB using Python, in Debian"

[taxonomies]
tags = ['Debian', 'Python', 'non-FLOSS']
+++

The following instructions assume that you are using [Debian Squeeze],
the current \'stable\' release. The instructions here are very specific,
so look [elsewhere] for something more generic.

**downloads**:

-   Get registered on Oracle website, and download
    oracle-instantclient11.2-basic\*.rpm (\~40MB).
-   Get [cx-Oracle] rpm for your specific Python version and your
    specific processor (in my case, 3.1 and i386 respectively).

**installation and setup**:

``` {.sourceCode .bash}
sudo apt-get install libpython3.1 libaio1 alien
sudo alien --install oracle-instantclient11.2-basic*rpm cx_Oracle*rpm
sudo ln -s /usr/lib/python3.1/site-packages/cx_Oracle.so /usr/lib/python3.1/lib-dynload
sudo ln -s /usr/lib/oracle/11.2/client/lib/libnnz11.so /usr/lib
sudo ln -s /usr/lib/oracle/11.2/client/lib/libclntsh.so.11.1 /usr/lib
echo export LD_LIBRARY_PATH=/usr/lib/oracle/11.2/client/lib >> ~/.bashrc
source ~/.bashrc
python3 -c 'import cx_Oracle'
```

If that last line executes without printing a message to the screen, the
install is most likely successful.

For basic usage, see [this tiny tutorial].

  [Debian Squeeze]: http://www.debian.org/releases/squeeze/
  [elsewhere]: http://agiletesting.blogspot.com/2005/05/installing-and-using-cxoracle-on-unix.html
  [cx-Oracle]: http://cx-oracle.sourceforge.net/
  [this tiny tutorial]: http://tshepang.net/basic-usage-of-python-with-oracle-db-in-debian
