import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
chances = 3


def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got it right")
    else:
        print("You got it wrong.")

ask_user_and_check_number()
