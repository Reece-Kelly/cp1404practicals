MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
LOWER_SCORE_LIMIT = 0
UPPER_SCORE_LIMIT = 100
PASSING_SCORE_THRESHOLD = 50
EXCELLENT_SCORE_THRESHOLD = 90


def main():
    """Get a score and determine and print a result based off the score and print stars * score."""
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
    """Print score * stars."""
    print("*" * score)


def get_valid_score():
    """Get a score between 0 and 100 inclusive."""
    score = int(input("Score: "))
    while score < LOWER_SCORE_LIMIT or score > UPPER_SCORE_LIMIT:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine result based off score."""
    if score < PASSING_SCORE_THRESHOLD:
        result = "Bad"
    elif score < EXCELLENT_SCORE_THRESHOLD:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
