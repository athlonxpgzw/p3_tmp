#!/usr/bin/env python3                             #  1
# encoding: utf-8                                  #  2
                                                   #  3
database = [                                       #  4
           ['albert',  '1234'],                    #  5
           ['dilbert', '4242'],                    #  6
           ['smith',   '7524'],                    #  7
           ['jones',   '9843']                     #  8
]                                                  #  9
username = input('User name: ')                    # 10
pin = input('PIN code: ')                          # 11
if [username, pin] in database: print('Access granted') # 12
