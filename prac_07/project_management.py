"""
Estimate time to complete: 2 hours
Actual time to complete:
"""
from project import Project
import datetime

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")
FILENAME = "projects.txt"


def main():
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
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


def save_projects(projects, filename):
    out_file = open(filename, "w")
    out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    out_file.close()


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage != 100]
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project}")


def filter_projects_by_date(projects):
    user_date_string = input("Show projects that start after date (dd/mm/yy): ")
    user_date = datetime.datetime.strptime(user_date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.is_greater_than_date(user_date):
            print(project)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, date_string, priority, cost_estimate, completion_percentage)
    projects.append(project)
    return projects


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
