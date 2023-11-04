import random

NUMBER_OF_RANDOM_NUMBERS = 6
RANDOM_NUMBER_MINIMUM = 1
RANDOM_NUMBER_MAXIMUM = 45


def main():
    """Generates a user-specified amount of sets of random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        random_numbers = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            random_number = (random.randint(RANDOM_NUMBER_MINIMUM, RANDOM_NUMBER_MAXIMUM))
            while random_number in random_numbers:
                random_number = (random.randint(RANDOM_NUMBER_MINIMUM, RANDOM_NUMBER_MAXIMUM))
            random_numbers.append(random_number)
        random_numbers.sort()
        print(" ".join(f"{random_number:2}" for random_number in random_numbers))


main()
