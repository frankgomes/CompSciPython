"""
Name: Frank Gomes
Lab: 10
Date: 11-10-20
Extra: see total.py
"""
while True:
    userinput = input()
    userinput = userinput.replace("[", "").replace("]", "")
    userlist = list()
    userlist = list(map(lambda x: int(x), userinput.split(",")))
    descending = True
    if len(userlist) == 1:
        print("True")
        continue
    for i in range(len(userlist) - 1):
        if userlist[i] > userlist[i+1]:
            continue
        else:
            descending = False
    print(descending)
