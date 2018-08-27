#!/usr/bin/env python3
# encoding: utf-8

import fileinput, random
fortunes = list(fileinput.input())
print(random.choice(fortunes))
