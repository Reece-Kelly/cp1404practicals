"""
Estimate time to complete: 2 hours
Actual time to complete:
"""
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("L")
        elif choice == "S":
            print("S")
        elif choice == "D":
            print("D")
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            print("U")
        else:
            print("Invalid choice.")
        choice = input(">>> ").upper()


main()
