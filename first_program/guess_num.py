from random import randint

num = randint(1, 10)
guess = 0
while int(guess) != num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess < num:
        print("To low!")
    elif guess > num:
        print("Too high!")
    elif guess == num:
        print(f"You guessed it! It's {num} You won!")
        replay = input("Do you want to keep playing? (y/n) ")
        if replay.casefold() == "y".casefold():
            num = randint(1, 10)
            guess = 0
        else:
            print("Thank you for playing!")
