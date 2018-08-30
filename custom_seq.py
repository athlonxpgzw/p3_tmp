#!/usr/bin/env python3
# encoding: utf-8

def check_index(key):
    '''
    pass
    '''
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError
class ArithmeticSequence:
    '''
    pass
    '''
    def __init__(self, start=0, step=1):
        '''
        pass
        '''
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        '''
        pass
        '''
        check_index(key)
        try: return self.changed[key]
        except KeyError:
            return self.start + key * self.step
    def __setitem__(self, key, value):
        '''
        pass
        '''
        check_index(key)
        self.changed[key] = value
