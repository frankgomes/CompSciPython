"""
Name: Frank Gomes
Lab: 8a
Date: 26-08-19
Extra: Launches other lab files from a menu
"""


# Python doesn't have switch-case statements so it's function switcher time
def launch(a):
    switcher = {
        1: __import__('bigorsmall'),
        2: __import__('addsubmult'),
        3: __import__('leap_year.py'),
        4: __import__('discount')
    }


a = int(input("Enter a number from 1 through 4: "))
launch(a)
