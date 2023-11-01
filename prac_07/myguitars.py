"""
Estimate to complete: 30 minutes
Start time: 11:10
Finish time:
"""
from guitar import Guitar


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        guitar_details = line.strip().split(",")
        guitar = Guitar(guitar_details[0], guitar_details[1], guitar_details[2])
        guitars.append(guitar)
    in_file.close()


main()
