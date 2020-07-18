+++
date = 2011-01-25
title = "shlex and subprocess"
[taxonomies]
tags = ['Python']
+++

I learned about a module called [shlex]. It's stated to be a simple
lexical analyzer, and I don't really know what this means, but I found
at least one of its uses. It provides a convenience method that lets me
split a command line string, to feed into [subprocess] module.

Let's say I want to run the command `/bin/cat 'file with spaces'` from
within `python`. A normal `split` won't work, because it uses white
space as a delimiter (by default). To test, I will create a file named
"**file with spaces**" and add text (`content of 'file with spaces'`).

``` {.sourceCode .sh}
$ echo 'content of file with spaces' > 'file with spaces'
```

And here's the code, using the normal split method:

``` {.sourceCode .python}
import subprocess
cmd = "/bin/cat 'file with spaces'"
formatted_cmd = cmd.split()
subprocess.Popen(formatted_cmd)
```

Output:

``` {.sourceCode .sh}
/bin/cat: 'file: No such file or directory
/bin/cat: with: No such file or directory
/bin/cat: spaces': No such file or directory
```

That's when `shlex` module gets to be useful.

``` {.sourceCode .python}
import shlex, subprocess
cmd = "/bin/cat 'file with spaces'"
formatted_cmd = shlex.split(cmd)
subprocess.Popen(formatted_cmd)
```

Output:

    content of 'file with spaces'

  [shlex]: http://docs.python.org/library/shlex.html
  [subprocess]: http://docs.python.org/library/subprocess.html
