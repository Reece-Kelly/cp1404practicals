from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Lets drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "d":
            pass
        if user_choice == "c":
            pass
        print(MENU)
        user_choice = input(">>> ").lower()

