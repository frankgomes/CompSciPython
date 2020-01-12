while True:
    userinput = input()
    if userinput.split(' ')[1] == "True":
        print(userinput.split(' ')[0].upper())
    else:
        print(userinput.split(' ')[0])
