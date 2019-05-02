greater_than_three = 5 > 3
print(greater_than_three)

print(6 > 5)

print(5 == 4)

numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers_array:
    if number > 5:
        print(number)

print(10 in numbers_array)
print(10 not in numbers_array)

magic_number = [3, 9]
user_number = 3
print(user_number in magic_number)

if user_number == 3 or user_number == 9:
    print(f"Your guess of {user_number} was correct")
else:
    print(f"Your number of {user_number} was incorrect.")
