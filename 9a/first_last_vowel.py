while True:
    userinput = input()
    if userinput[0] in "aeiou":
        if userinput[-1] in "aeiou":
            print("yes")
        else:
            print("no")
    else:
        print("no")
