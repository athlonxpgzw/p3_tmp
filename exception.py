#!/usr/bin/env python3
# encoding: utf-8

while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        print(x / y)
    except:
        print("Invalid input, Please try again")
    else:
        break
