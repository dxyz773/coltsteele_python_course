# Rock Paper Scissors
from random import choice, randint

intro = "\n_🪨 Rock!_________________________\n_________Paper! 📄_______________\n___________________🔪 Scissors!__\n_________           _____________\n_________💥 SHOOT! 💥____________\n_________________________________\n"


def rock_paper_scissors():
    print(intro)
    moves = [None, "Rock 🪨", "Paper 📄", "Scissors 🔪"]
    machine_choice = randint(1, 3)
    user_choice = input("YOU CHOOSE 1:[ 🪨 ], 2:[ 📄 ], or 3:[ 🔪 ]\n")
    results = ["YOU WIN! 🏆", "YOU LOSE! 🤡", "🏳️ IT'S A DRAW! 🏳️"]
    result_str = "You chose {}. The machine chose {}. {}"

    if not user_choice == "1" and not user_choice == "2" and not user_choice == "3":
        print("Please enter a valid number choice")
        rock_paper_scissors()
    else:
        print(user_choice)

        print(machine_choice)
        win_message = result_str.format(
            moves[int(user_choice)], moves[int(machine_choice)], results[0]
        )
        lose_message = result_str.format(
            moves[int(user_choice)], moves[int(machine_choice)], results[1]
        )
        draw_message = result_str.format(
            moves[int(user_choice)], moves[int(machine_choice)], results[2]
        )

        if int(user_choice) == machine_choice:
            print(draw_message)
            play_again = input("Want to play again? y/n\n")
            if play_again == "y" or play_again == "Y" or play_again == "yes":
                rock_paper_scissors()
            else:
                return
        elif int(user_choice) == 1:
            if machine_choice == 3:
                print(win_message)
            else:
                print(lose_message)
        elif int(user_choice) == 2:
            if machine_choice == 1:
                print(win_message)
            else:
                print(lose_message)
        elif int(user_choice) == 3:
            if machine_choice == 2:
                print(win_message)
            else:
                print(lose_message)

        play_again = input("Want to play again? y/n\n")
        if play_again == "y" or play_again == "Y" or play_again == "yes":
            rock_paper_scissors()
        else:
            return

    # rock > scis, scis > paper, paper > rock
    # 1 > 3,         3 > 2       2 > 1

    # user > machine 1 > 3 - DONE   3 > 2 - DONE   2 > 1 - DONE
    # user < machine 3 < 1 - DONE   2 < 3 - DONE   1 < 2 - DONE


rock_paper_scissors()
