"""
Name: Frank Gomes
Lab: 9a
Extra: Shifts characters forwards or backwards
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
while True:
    userinput = input()
    shift = int(userinput.split(", ")[1])
    base = userinput.split(", ")[0]
    direction = userinput.split(", ")[2]
    for i in range(1, (len(base) - 1)):
        if direction == "forward":
            print(alphabet[alphabet.index(base[i]) + shift], end='')
        elif direction == "backward":
            print(alphabet[alphabet.index(base[i]) - shift], end='')
    print()
