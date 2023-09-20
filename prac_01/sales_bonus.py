"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

UNDER_1000_BONUS_RATE = 0.1
OVER_1000_BONUS_RATE = 0.15

sales = float(input("Sales: $"))
bonus = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * UNDER_1000_BONUS_RATE
    else:
        bonus = sales * OVER_1000_BONUS_RATE
    print(f"Bonus: ${bonus}")
    sales = float(input("Sales: $"))
