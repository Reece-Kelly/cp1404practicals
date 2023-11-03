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
    projects = []
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("F")
        elif choice == "A":
            print("A")
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects():
    filename = input("Filename: ")
    in_file = open(filename, "r")
    projects = []
    in_file.readline()
    for line in in_file:
        project_details = line.strip().split("\t")
        project = Project(project_details[0], project_details[1], int(project_details[2]), float(project_details[3]),
                          int(project_details[4]))
        projects.append(project)
    in_file.close()
    print(f"{len(projects)} projects loaded.")
    return projects


def save_projects(projects):
    filename = input("Filename: ")
    out_file = open(filename, "w")
    out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    out_file.close()


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print(f"\t{project}")
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print(f"\t{project}")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[project_choice].completion_percentage = new_percentage
    projects[project_choice].priority = new_priority
    return projects


main()
