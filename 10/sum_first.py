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
    greatersum = 0
    for i in userlist:
        if int(i) > int(userlist[0]):
            greatersum += int(i)
    if greatersum == 0:
        greatersum = -1
    print(greatersum)
