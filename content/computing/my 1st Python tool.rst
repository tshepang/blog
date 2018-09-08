---
date: '2008-11-07'
tags: Python
title: my 1st Python tool
---

A senior of mine at my current job has asked me to write a tool to
convert from [UFF format] to csv for easy spreadsheet processing,
producing results that proved most beneficial to me (the path towards
code mastery). The tool is less than 200 lines of Python code, and I
even got a peek at the necessary changes to have it run on Python 3 (and
successfully doing so), as well as experiencing the relatively
unchallenging problems of getting it to run on Windows XP (it was
developed on Debian). Of course I would not have bothered had the
requirement not been getting it to run on that most popular of end-user
OSes. But Python\'s cross-platform nature makes it easy, and their work
on getting the supporting suite (installer, IDE, Python shell) easy to
install and run on Windows deserves serious respect.

By the way I haven\'t so far learned the importance/use of classes so
the entire thing is in functions. And the code is also extremely slow
(and even slower on WinXP) and only does basic checks for the validity
of the source file to be processed so will loudly crash on corrupted
files. Other than that, the tool is pretty robust and made my \'client\'
real happy, considering the previous tool was really broken by design (a
pain to work with, being muddled with severe limitations) and also
relied on Matlab being installed.

  [UFF format]: http://en.wikipedia.org/wiki/Universal_File_Format
