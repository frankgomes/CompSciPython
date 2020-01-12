"""
Name: Frank Gomes
Lab: 9a
Extra: see caesarCipher.py
"""
while True:
    userinput = input()
    pairs = 0
    for i in range(1, len(userinput)):
        if userinput[i-1] == userinput[i]:
            pairs += 1
    print(pairs)
