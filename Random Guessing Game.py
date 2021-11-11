import random


def main():
    guess_counts = 1
    guess_no = random.randint(1, 15)
    user_guess = int(input("Guess the number:"))
    while guess_no != user_guess:
        result = method1(guess_no, user_guess)
        print(result)
        guess_counts += 1
        user_guess = int(input("Guess the number:"))
    print("Congratulations!")
    print("Guess counts:", guess_counts)


def method1(guess_no, user_guess):
    if guess_no > user_guess:
        return "Too low,try again."
    else:
        return "Too high, try again"


main()