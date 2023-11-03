"""
Estimate time to complete: 2 hours
Actual time to complete:
"""
from project import Project

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
            projects = load_projects()
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


def load_projects():
    filename = input("Filename: ")
    in_file = open(f"{filename}", "r")
    projects = []
    in_file.readline()
    for line in in_file:
        project_details = line.strip().split("\t")
        project = Project(project_details[0], project_details[1], project_details[2], project_details[3],
                          project_details[4])
        projects.append(project)
    in_file.close()
    return projects


main()
