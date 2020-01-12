'''
Name: Frank Gomes
Date: 06-01-20
Lab: 9b
Extra:
'''

while True:
    # Take array from user
    userinput = input()
    # Variable to hold sum of all array items
    sum = 0
    # Remove '[' and ']' from input and split remaining string at all commas, making an array of the values inbetween
    array = userinput.replace("[","").replace("]","").split(",")
    # For every item in the array, add it to the sum
    for i in array:
        sum = sum + int(i)
    # Print final sum
    print(sum)

