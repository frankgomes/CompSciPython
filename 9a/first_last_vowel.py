"""
Name: Frank Gomes
Lab: 9a
Extra: see caesarCipher.py
"""
while True:
    userinput = input()
    if userinput[0] in "aeiouAEIOU":
        print("yes")
    elif userinput[-1] in "aeiouAEIOU":
        print("yes")
    else:
        print("no")
