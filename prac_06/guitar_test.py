from guitar import Guitar


def main():
    gibson = Guitar("Gibson", 1922, 16035.40)
    epiphone = Guitar("Epiphone", 2004, 500)

    print(f"Gibson get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"Epiphone get_age() - Expected 19. Got {epiphone.get_age()}")
    print(f"Gibson is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"Epiphone is_vintage() - Expected False. Got {epiphone.is_vintage()}")


main()
