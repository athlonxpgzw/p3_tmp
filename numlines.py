#!/usr/bin/env python3
# encoding: utf-8

import fileinput

for line in fileinput.input(inplace = True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50} # {:2d}'.format(line, num))
