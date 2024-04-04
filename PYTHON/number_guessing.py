
# import random
# import math
# print("Welcome to Number Guessing Game!\n")
# lower = int(input("Enter Lower Bound : "))
# upper = int(input("Enter Upper Bound : "))

# x = random.randint(lower,upper)
# print()
# print("You have only",round(math.log(upper - lower + 1, 2)),"chances to guess the number.\n")

# attempts = 0
# while attempts < math.log(upper - lower + 1, 2):
#     attempts += 1
#     guess = int(input("Enter your guess : "))
#     if x == guess:
#         print("\nCongratulations! You've guessed the number in ",attempts ,"attempts.")
#         break
#     elif x > guess:
#         print("Too low! Try again.")
#     elif x < guess:
#         print("Too high! Try again.")
        

# if attempts >= math.log(upper - lower + 1, 2):
#     print("\nThe number is %d" % x)
#     print("\nBetter Luck Next time!")


