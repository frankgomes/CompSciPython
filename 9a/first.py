"""
Name: Frank Gomes
Lab: 9a
Extra: see caesarCipher.py
"""
while True:
    userinput = input()
    first_char = userinput[0]
    userinput = userinput.replace(first_char, '', 1)
    if first_char in userinput:
        print("yes")
    else:
        print("no")
