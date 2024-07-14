while True:
    try:
        num = int(input("please enter a number: "))
    except ValueError:
        print("That is not a number!")
    else:
        print("Good job! You entered a number")
        break
    finally:
        print("I run always")

print("REST OF GAME LOGIC RUNS")
