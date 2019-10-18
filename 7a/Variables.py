'''
Name: Frank Gomes
Lab: 7a
Date: 15-10-19
Extra: Run your own code at the end
'''

# Prompt user for their info
name = str(raw_input("What is your name? "))
age = str(raw_input("How old are you? "))
year = str(raw_input("What year was your last birthday? "))
print ("Your name is " + name + " and you are " + age + " years old.\nYou were born in " + str(int(year) - int(age)) +
       ".")
# Cool extra
input("Enter some code to run. ")
