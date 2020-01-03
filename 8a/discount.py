"""
Name: Frank Gomes
Lab: 8a
Date: 26-08-19
Extra: see main.py
"""


def discount():
    while True:
        amount = float(input())
        if amount > 2000:
            print(amount * 0.9)
        else:
            print(amount)


discount()
