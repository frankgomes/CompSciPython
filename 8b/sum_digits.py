while True:
    userinput = input()
    sum = 0
    for i in range(0, len(userinput)):
       sum += int(userinput[i])
    print(sum)
