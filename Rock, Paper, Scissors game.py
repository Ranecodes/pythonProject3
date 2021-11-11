import random
import math


def main():
    computer_choice = random.choice(['r', 's', 'p'])
    user_entry = input("Rock(type 'r'), Paper(type 'p'), Scissors(type 's')?")
    user_entry = user_entry.lower()
    if computer_choice == user_entry:
        return(0, user_entry, computer_choice)

    if is_win(computer_choice, user_entry):
        return (1, user_entry, computer_choice)

    return (-1, user_entry, computer_choice)



def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (
            player == "s" and opponent == "p"):
        return True
    return False


def best_of_win(n):
    player_win, computer_win = 0, 0
    wins_necessary = math.ceil(n / 2)
    while player_win < wins_necessary and computer_win < wins_necessary:
        result, user_entry, computer_choice = main()
        if result == 0:
            print(f"It is a tie. You and the computer have both chosen {computer_choice}.")
        elif result == 1:
            player_win += 1
            print(f"You chose {user_entry} and the computer chose {computer_choice}. You won!")
        else:
            computer_win += 1
            print(f"You chose {user_entry} and the computer chose {computer_choice}.You lost :( ")
    if player_win > computer_win:
        print(f"You have won the best of {n} games! Congratulations!")
    else:
        print(f"Computer won best out of {n} games. Better luck next time :(")


if __name__ == '__main__':
    best_of_win(3)
