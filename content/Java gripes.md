+++
date = 2011-11-02
tags = ['non-Python', 'Python']
title = "Java gripes"
+++

Okay, so Java sucks \'a bit\', but the following surprised me:

-   I struggled to find a way to count the number of elements in an
    array. In a string it\'s done thus: `"four".length()`. Given that, I
    expected that `{'f', 'o', 'u', 'r'}.length()` would gimme the same
    result. Nah! I found that I had to do
    `new char [] {'f', 'o', 'u', 'r'}.length`, and yes, without the
    brackets after length. WTF! There might be a good reason for such
    (seeming) inconsistency of course, but I\'ve been spoilt by
    Python\'s elegant equivalents: `len("four")` and
    `len(['f','o', 'u', 'r'])` which all give the same result.
    (sidenote: `len()` is a Python built-in function, which explains why
    there\'s no dot notation there).
-   The standard library doesn\'t have CSV handling! I had to find an
    external library for that!
-   Given 2 strings, I can\'t do `str1==str2` for comparison, but am
    forced to use the string method, equals: `str1.equals(str2)`. This
    bit me a few times, and am sure am not the only one.
-   The standard library doesn\'t have `.INI` file handling ([Someone
    pointed to a 3rd party library]).

  [Someone pointed to a 3rd party library]: http://stackoverflow.com/questions/3728823
