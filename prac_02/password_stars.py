MINIMUM_LENGTH = 5


def main():
    """Get valid password and print asterisks * password length"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisk * password length."""
    print("*" * len(password))


def get_password():
    """Get valid password."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short")
        password = input("Password: ")
    return password


main()
