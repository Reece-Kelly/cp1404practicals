from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program that allows the user to choose and drive taxis before displaying their total bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    chosen_taxi = None
    print("Lets drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                chosen_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == "d":
            if chosen_taxi:
                chosen_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                chosen_taxi.drive(distance_to_drive)
                print(f"Your {chosen_taxi.name} trip cost you ${chosen_taxi.get_fare()}")
                total_bill += chosen_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill}")
        print(MENU)
        user_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display each taxi in a list of taxi with a number for each object."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
