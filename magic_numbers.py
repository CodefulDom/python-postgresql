import random

# magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
# chances = 3

# for attempt in range(chances):
#     print(f"This is attempt {attempt + 1}")
#     user_number = input("Enter a Number between 0 and 9: ")

#     if int(user_number) in magic_numbers:
#         print(f"{user_number} was correct")
#     else:
#         print(f"{user_number} was an incorrect guess. Try Again!")

minimum = 100
for index in range(10):
    random_number = random.randint(0, 100)
    print(f"The number generatred was {random_number}")
    if random_number <= minimum:
        minimum = random_number
        print(f"the minimum is {minimum}")
