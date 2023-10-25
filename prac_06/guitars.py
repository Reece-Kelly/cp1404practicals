from guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost} added.\n")
    name = input("Name: ")
print("\n... snip ...\n")
