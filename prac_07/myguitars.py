"""
Estimate time to complete: 30 minutes
Actual time to complete: 42 minutes
"""
from guitar import Guitar


def main():
    """
    Load and display a list of guitars from a file and allow the user to add to the list before saving it to a file.
    """
    guitars = load_guitars()
    print("Unsorted guitars:")
    for guitar in guitars:
        print(guitar)
    print("\nSorted guitars:")
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")
    save_guitars(guitars)


def load_guitars():
    """Load a list of guitars from a file and create a list of guitar objects."""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        guitar_details = line.strip().split(",")
        guitar = Guitar(guitar_details[0], guitar_details[1], guitar_details[2])
        guitars.append(guitar)
    in_file.close()
    return guitars


def save_guitars(guitars):
    """Save a list of guitar objects to a file."""
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        string = f"{guitar.name},{guitar.year},{guitar.cost}\n"
        out_file.write(string)
    out_file.close()


main()
