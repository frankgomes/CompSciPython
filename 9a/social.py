"""
Name: Frank Gomes
Lab: 9a
Extra: see caesarCipher.py
"""
while True:
    userinput = input()
    if userinput[3] == '-':
        if userinput[6] == '-':
            print(userinput[7:])
        else:
            print("bad")
    else:
        print("bad")
