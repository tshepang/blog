errors resulting from setting named pipes to be non-blocking
============================================================

:date: 2012-11-18
:tags: non-Python



Using C language, I have been writing to named pipes in a non-blocking
way and have been getting a whole bunch of EAGAIN errors. I have spent
way too long on the web trying to find out why, and bumped onto `this
excellent answer`_. The specific part is where I was writing to a pipe
which wasn't read and would therefore block if it wasn't told not to.
Looking at the manpage, I see that this would give the same value as
EWOULDBLOCK, which is a far more meaninful name in this case.

This is what will display those errors:

.. code-block:: c

    if (write(fd, buffer, strlen(buffer)) == -1)
        printf( "error writing to file '%s': %s (errno %d)",
                 path, strerror(errno), fd);
    }

And here is how to avoid them:

.. code-block:: c

    if ((write(fd, buffer, strlen(buffer)) == -1) && (errno != EWOULDBLOCK)) {
        printf( "error writing to file '%s': %s (errno %d)",
                 path, strerror(errno), fd);
    }

I probably should use ``perror`` or ``fprintf(stderr, ...)`` instead of
a ``printf`` there.

Anyways, to avoid this kind of confusion, I just wish these two
variables did not refer to the same errno value.


.. _this excellent answer: http://developerweb.net/viewtopic.php?pid=25967#p25967
