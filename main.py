# Thayer Yang
# 07 JAN 2025
# Passing Returns in Functions

from random import randint as r

def rand_num():
    """Returns a random number between 1 and 25"""
    num = r(1,26)
    return num

def get_user_input():
    """Gets a number input from the user"""
    while True:
        num = input("Enter a number:\n")
        if num.isdigit():
            return int(num)
        else:
            print("Error: Input is not an integer")

def square(num: int):
    """Squares the number inputted"""
    return num**2

random_number = rand_num()

user_num = get_user_input()

random_sq = square(random_number)
user_sq = square(user_num)

print(f"""Random Number: {random_number}
Random Number Squared: {random_sq}
User Number: {user_num}
User Number Squared: {user_sq}""")
