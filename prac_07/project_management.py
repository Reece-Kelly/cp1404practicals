"""
Estimate time to complete: 2 hours
Actual time to complete: 4 hours and 35 minutes
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
    """Load, display, add to, update, and save a list of projects."""
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
    """Load projects from a file and return a list of project objects."""
    try:
        in_file = open(filename, "r")
        projects = []
        in_file.readline()
        for line in in_file:
            project_details = line.strip().split("\t")
            project = Project(project_details[0], project_details[1], int(project_details[2]),
                              float(project_details[3]),
                              int(project_details[4]))
            projects.append(project)
        in_file.close()
        print(f"{len(projects)} projects loaded.")
        return projects
    except FileNotFoundError:
        print("File not found.")


def save_projects(projects, filename):
    """Save a list of project objects to a file."""
    try:
        out_file = open(filename, "w")
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
        out_file.close()
    except TypeError:
        print("Invalid file choice.")


def display_projects(projects):
    """Display a list of projects in sections of incomplete projects and complete projects."""
    incomplete_projects = sorted([project for project in projects if project.completion_percentage != 100])
    complete_projects = sorted([project for project in projects if project.completion_percentage == 100])
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"\t{project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a user specified date."""
    try:
        user_date_string = input("Show projects that start after date (dd/mm/yy): ")
        user_date = datetime.datetime.strptime(user_date_string, "%d/%m/%Y").date()
        past_user_date_projects = sorted([project for project in projects if project.start_date > user_date])
        for project in past_user_date_projects:
            print(project)
    except ValueError:
        print("Invalid date.")


def add_project(projects):
    """Add a new project object to projects list."""
    try:
        print("Let's add a new project")
        name = input("Name: ")
        date_string = input("Date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
        project = Project(name, date_string, priority, cost_estimate, completion_percentage)
        projects.append(project)
        return projects
    except ValueError:
        print("Invalid Input.")
        return projects


def update_project(projects):
    """Update the percentage and priority of a project."""
    try:
        for i, project in enumerate(projects):
            print(f"{i} {project}")
        project_choice = int(input("Project choice: "))
        print(projects[project_choice])
        new_percentage = input("New Percentage: ")
        if new_percentage != "":
            projects[project_choice].completion_percentage = int(new_percentage)
        new_priority = input("New Priority: ")
        if new_priority != "":
            projects[project_choice].priority = int(new_priority)
        return projects
    except ValueError:
        print("Invalid Input.")
        return projects


main()
