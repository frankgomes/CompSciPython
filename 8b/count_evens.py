while True:
    userinput = input()
    sum = 0
    evens = 0
    odds = 0
    for i in range(0, len(userinput)):
        if int(userinput[i]) % 2 == 0:
            evens += 1
    print(evens)
