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
    userlist.sort()
    print(userlist[0])
