#!/usr/bin/env python3
# encoding: utf-8

def square(x):
    '''
    caculate square
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x ** 2

def product(x, y):
    return x * y

if __name__ == '__main__':
    import doctest, my_math
    doctest.testmod(my_math)
