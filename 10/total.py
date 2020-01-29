"""
Name: Frank Gomes
Lab: 10
Date: 11-10-20
Extra: displays both sum & average in total.py
"""
while True:
    userinput = input()
    userinput = userinput.replace('[','')
    userinput = userinput.replace(']','')
    numbers = userinput.split(',')
    number_sum = 0
    for i in numbers:
        number_sum += int(i)
    print("Sum: {0}, Avg.: {1}".format(number_sum, number_sum / len(numbers)))
