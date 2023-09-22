MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
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
    print("*" * score)


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
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
