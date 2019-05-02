magic_numbers = [1, 3, 7]
chances = 3

for attempt in range(chances):
    print(f"This is attempt {attempt + 1}")
    user_number = input("Enter a Number between 0 and 9: ")

    if int(user_number) in magic_numbers:
        print(f"{user_number} was correct")
    else:
        print(f"{user_number} was an incorrect guess. Try Again!")
