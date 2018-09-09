+++
date = 2011-03-15
tags = ['non-Python', 'Python']
title = "cat, Python, and Perl"
+++

I came across [a tutorial] that showes how to implement a simple cat in
Perl. I\'ve modified their example for the sake of simplicity:

``` {.sourceCode .perl}
sub cat {
    foreach my $filename (@_) {
        open FILE, $filename;
        while (my $line = <FILE>) {
            print $line;
        }
    }
}
cat @ARGV;
```

Running this script (e.g. `perl cat.pl file`) will display those files
as if you ran `cat file`.

I decided to see how the Python example would look like:

``` {.sourceCode .python}
import sys
def cat(files):
    for filename in files:
        with open(filename) as FILE:
            for line in FILE:
                print(line, end="")
cat(sys.argv[1:])
```

Running this script (e.g. `python3 cat.py file1 file2`) will give
exactly the same result as above.

notes
=====

-   The Perl keyword, `my`, indicates that the variabe it refers to is
    local. Without that, it\'s taken to be global. As for Python, this
    is implicit, and depends on where the variable is placed (scope).
-   Perl has special ways of identifying data types. In our example, `$`
    is used to identify a variable that has a single value, and is known
    as a scalar in Perl talk. This can be tedious of course (so much
    typing!). In Python, the data fed into the variable is the only
    thing that determines what type of the variable it is. I see this as
    noise from Perl. It results in some badness, as in you can have two
    variables names be the same, but given different types (e.g.
    `my $var; my @var;`)
-   The upper case file handler, `FILE`, is a matter of convention for
    Perl, and can be named \'anything\'. I used it in the Python sample
    only for the sake of clarity.
-   The `<>` operator is special syntax that means a file is being
    manipulated. Python has no such.
-   The `@_` is an argument list (`@ARGV`) from the function call,
    `cat`. This is one other thing that is implicit about Perl, where
    you have to learn extra syntax (and concepts), where a simple
    argument list should have been provided during the function
    declaration, as in Python\'s `cat(files)`.
-   Note that I didn\'t need to import anything to get Perl to work with
    command line arguments. With Python, I need to explicitly do so, and
    that\'s via the [sys module], which is part of its standard library.
-   The Python `with` statement is meant to make our lives easier, but
    also adds syntax to the language. What it does is close a file for
    us so we don\'t have to do it.
-   The Python `print()` function adds a newline by default, and that
    would results in ugly output from our code, that\'s why we used the
    `end=""`.
-   The `[1:]` from the last statement in the Python example means that
    we are slicing the list, removing the first element (element 0), and
    keeping everything else. We do this because the current running
    script is considered by Python as element 0, while in Perl, the 1st
    element is actually the first thing that appears on the command line
    after the script name. One would say that Perl does this more
    elegantly.

further reading
===============

-   [Python scope]
-   [Python print function]
-   [Python with statement]

  [a tutorial]: http://greenteapress.com/perl/perl.pdf
  [sys module]: http://docs.python.org/3/library/sys
  [Python scope]: http://docs.python.org/reference/executionmodel
  [Python print function]: http://docs.python.org/3/library/functions#print
  [Python with statement]: http://docs.python.org/3/reference/compound_stmts#the-with-statement
