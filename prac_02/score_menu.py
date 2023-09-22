MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Get a score and determine and print a result based off the score and print stars * score"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you and Goodbye!")


def print_stars(score):
    """Print score * stars"""
    print("*" * score)


def get_valid_score():
    """Get a score between 0 and 100 inclusive"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine result based off score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
