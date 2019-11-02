"""
Name: Frank Gomes
Lab: 7a
Date: 15-10-19
Extra: See Variables.py
"""

while True:
    num = float(raw_input("Enter a numerator: "))
    den = float(raw_input("Enter a denominator: "))
    print (num/den)
    print '{0}/{1} = {2}'.format(int(num), int(den), float(num/den))
