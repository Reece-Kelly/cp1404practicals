NUMBER_OF_NUMBERS = 5


def main():
    """Get a list of numbers and display information about them."""
    numbers = []
    for i in range(NUMBER_OF_NUMBERS):
        number = int(input(f"Enter number: "))
        numbers.append(number)
    print_number_information(numbers)


def print_number_information(numbers):
    """Print the first, last, smallest, largest numbers of a list and the average"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()


def main_2():
    """Check if username is in username list"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main_2()
