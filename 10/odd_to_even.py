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
    firstodd = -1
    firsteven = -1
    for i in range(len(userlist)):
        if int(userlist[i]) % 2 == 1:
            firstodd = i
            break
    for i in range(len(userlist)):
        if int(userlist[i]) % 2 == 0:
            firsteven = i
            break
    if firstodd == -1 or firsteven == -1:
        print(-1)
        continue
    print(abs(firsteven - firstodd))
