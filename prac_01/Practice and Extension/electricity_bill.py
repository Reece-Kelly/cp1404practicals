TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
# cents_per_kwh = int(input("Enter cents per kWh: "))
daily_use_in_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
bill = tariff_choice * daily_use_in_kwh * number_of_billing_days / 100
print(f"Estimated bill: ${bill:.2f}")
