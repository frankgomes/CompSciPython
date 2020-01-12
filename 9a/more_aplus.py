while True:
    userinput = input()
    if "aplus" in userinput:
        userinput = userinput.replace("aplus", '', 1)
        if "aplus" in userinput:
            print("yes")
        else:
            print("no")
    else:
        print("no")
