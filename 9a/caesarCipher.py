# List in alphabetical order
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
while True:
    userinput = input()
    shift = int(userinput.split(", ")[1])
    base = userinput.split(", ")[0]
    for i in range(1, (len(base) - 1)):
        print(alphabet[alphabet.index(base[i]) - shift], end='')
    print()
