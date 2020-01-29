"""
Name: Frank Gomes
Lab: 10
Date: 11-10-20
Extra: see total.py
"""


def findrepeats(toparse: list) -> int:
    mem = None
    currhertz: int = 0
    for ele in toparse:
        if x := toparse.count(ele) > currhertz:
            currhertz = x
            mem = ele
        else:
            pass

    return mem


while True:
    userinput = input()
    userinput = userinput.replace("[", "").replace("]", "")
    userlist = list()
    userlist = list(map(lambda x: int(x), userinput.split(",")))
    print(findrepeats(userlist))
