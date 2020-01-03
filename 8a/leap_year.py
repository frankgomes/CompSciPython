"""
Name: Frank Gomes
Lab: 8a
Date: 26-08-19
Extra: see main.py
"""


def leap_year():
    while True:
        year = int(input())
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("True")
                else:
                    print("False")
            else:
                print("True")
        else:
            print("False")


leap_year()
