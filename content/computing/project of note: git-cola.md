---
date: '2013-10-17'
tags: 'project-of-note, VCS'
title: 'project of note: git-cola'
---

I use [git-cola] mostly when I want to commit various hunks separately;
it makes that task real easy.

I was impressed by its equivalent functionality for the git `--amend`
option the first time I saw it. If you click on the **Amend Last
Commit** radio button, it actually displays the commit message of that
previous commit. I was surprised to see it, especially since on clicking
that option, I quickly ran to the command-line to copy that commit
message, only to see the message waiting for me, ready to be edited
away.

Another feature I really like is that if you attempt to commit something
without staging it first, instead of just complaining, if offers to
*stage and commit* all in one click. Nice.

These functionalities are real simple, but they really make for a
pleasant user experience. Pity I haven\'t seen a tool as easy to use in
the land of Mercurial. There, I use the command-line `hg record` which
isn\'t as pleasant.

  [git-cola]: http://git-cola.github.io
