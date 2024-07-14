for x in range(1, 21):
    if x % 2 == 0 and not x == 4:
        print(f"{x} is even")
    elif x % 2 != 0 and not x == 13:
        print(f"{x} is odd")
    elif x == 4 or x == 13:
        print(f"{x} is UN-LUCKY!")
