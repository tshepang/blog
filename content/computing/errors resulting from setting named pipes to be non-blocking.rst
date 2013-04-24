errors resulting from setting named pipes to be non-blocking
============================================================

:date: 2012-11-18
:tags: non-Python



Using C, I have been writing to named pipes in a non-blocking
way and have been getting a whole bunch of EAGAIN errors.
I have spent way too long on the web trying to find out why,
and bumped onto `this excellent answer`_.
Looking at the manpage, I see that this would give the same value as
EWOULDBLOCK, which is a far more meaningful name in this case.

This is what will display those errors:

.. code-block:: c

    if (write(fd, buffer, strlen(buffer)) == -1)
        fprintf (stderr, "error writing to file '%s': %s (errno %d)",
                 path, strerror(errno), fd);
    }

And here is how to avoid them:

.. code-block:: c

    if ((write(fd, buffer, strlen(buffer)) == -1) && (errno != EWOULDBLOCK)) {
        fprintf( stderr, "error writing to file '%s': %s (errno %d)",
                 path, strerror(errno), fd);
    }

To avoid this kind of confusion, I just wish these two
variables did not refer to the same errno value.


__ http://developerweb.net/viewtopic.php?pid=25967#p25967
