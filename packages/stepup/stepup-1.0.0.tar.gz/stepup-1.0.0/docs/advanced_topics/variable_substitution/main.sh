#!/usr/bin/env bash
git clean -dfX .
unset STEPUP_ROOT
MYVAR=foo stepup -n -w 1 | sed -f ../../clean_stdout.sed > stdout.txt
