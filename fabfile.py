#!/bin/bash -e

OUTPUTDIR='.output'
gutenberg build
cp public/* $OUTPUTDIR
cd $OUTPUTDIR
git add --all
git commit --message "build"
git push origin master
hg push
