OVER_100_DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total += price_of_item
if total > 100:
    total -= total * OVER_100_DISCOUNT_RATE
print(f"Total price for {number_of_items} is ${total:.2f}")
