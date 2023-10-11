def main():
    """Get a name from an email and create a dictionary of email to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        username = email.split("@")[0]
        name_parts = username.split('.')
        name = " ".join(name_parts).title()
        name_confirmation_choice = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation_choice != "Y" and name_confirmation_choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()

