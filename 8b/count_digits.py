while True:
    num = int(input())
    digits = 1
    while num > 0:
        num -= num % (10 ** digits)
        digits += 1
    print(digits - 1)
