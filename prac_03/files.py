# Question 1
# name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()

# Question 2
# in_file = open("name.txt", "r")
# name = in_file.readline()
# print(f"Your name is {name}")
# in_file.close()

# Question 3
# in_file = open("numbers.txt", "r")
# first_number = int(in_file.readline())
# second_number = int(in_file.readline())
# result = first_number + second_number
# print(f"Result: {result}")
# in_file.close()

# Question 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(in_file.readline())
print(f"Total: {total}")

