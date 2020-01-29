"""
Name: Frank Gomes
Lab: 10
Date: 11-10-20
Extra: see total.py
"""
while True:
    userinput = input()
    userinput = userinput.replace("[", "").replace("]", "")
    userlist = userinput.split(",")
    last = userlist[-1]
    del userlist[-1]
    lastrepeats = False
    for i in userlist:
        if i == last:
            lastrepeats = True
    print(lastrepeats)
