import random

NUMBER_OF_RANDOM_NUMBERS = 6

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        print(random.randint(1, 45), end=" ")
    print()
