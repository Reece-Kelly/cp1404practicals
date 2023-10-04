import random

NUMBER_OF_RANDOM_NUMBERS = 6
RANDOM_NUMBER_LOWER = 1
RANDOM_NUMBER_UPPER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        random_numbers = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            random_number = (random.randint(RANDOM_NUMBER_LOWER, RANDOM_NUMBER_UPPER))
            while random_number in random_numbers:
                random_number = (random.randint(RANDOM_NUMBER_LOWER, RANDOM_NUMBER_UPPER))
            random_numbers.append(random_number)
        random_numbers.sort()
        print(random_numbers)
        print()


main()
