#!/usr/bin/env python3
# encoding: utf-8

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print("Wordcount: ", wordcount)
