actual_price = int(input("Enter the actual value of the property: "))

assessment_price = actual_price * 0.6

tax = (assessment_price / 100) * 0.72

print(f"The assessment value of the house is ${assessment_price:.2f}.")
print(f"The tax for the acre accessed at ${assessment_price} is ${tax:.2f}.")