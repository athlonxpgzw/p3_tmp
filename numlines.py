#!/usr/bin/env python3                             #  1
# encoding: utf-8                                  #  2
                                                   #  3
import fileinput                                   #  4
                                                   #  5
for line in fileinput.input(inplace = True):       #  6
    line = line.rstrip()                           #  7
    num = fileinput.lineno()                       #  8
    print('{:<50} # {:2d}'.format(line, num))      #  9
