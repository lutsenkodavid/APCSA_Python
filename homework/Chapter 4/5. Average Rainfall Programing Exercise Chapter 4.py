years = int(input("Enter the number of years: "))
total = 0

for year in range(1, years + 1):
    for month in range(1, 13):
        print("Year", year, "Month", month)
        rain = float(input("How much rainfall this month? "))
        total += rain

months = years * 12
average = total / months

print("\nAfter", months, "months, the total rainfall was", total, "inches.")
print("The average rainfall per month was", average, "inches.")