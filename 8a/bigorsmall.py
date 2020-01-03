"""
Name: Frank Gomes
Lab: 8a
Date: 26-08-19
Extra: see main.py
"""


def bigorsmall():
    while True:
        a = int(input())
        b = int(input())
        if a > b:
            print("yes")
        elif a == b:
            print("aplus")
        elif a < b:
            print("no")


bigorsmall()
