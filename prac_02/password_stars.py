minimum_length = 5
password = input("Password: ")
while len(password) < minimum_length:
    print("Password is too short")
    password = input("Password: ")
print("*" * len(password))
