"""
Name: Frank Gomes
Lab: 8a
Date: 26-08-19
Extra: see main.py
"""


def addsubmult():
    while True:
        a = float(input())
        b = float(input())
        if a > b:
            print(a - b)
        elif a == b:
            print(a * b)
        elif a < b:
            print(b - a)


addsubmult()
