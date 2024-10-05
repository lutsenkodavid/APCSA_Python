loan_payment = float(input("Enter your monthly loan payment: "))
insurance = float(input("Enter your monthly insurance cost: "))
gas = float(input("Enter your monthly gas cost: "))
oil = float(input("Enter your monthly oil cost: "))
tires = float(input("Enter your monthly tires cost: "))
maintenance = float(input("Enter your monthly maintenance cost: "))


    
total_monthly_cost = (loan_payment + insurance + gas + oil + tires + maintenance) 
total_yearly_cost = (loan_payment + insurance + gas + oil + tires + maintenance) * 12

print(f"Your total monthly cost is ${total_monthly_cost}.")
print(f"Your total yearly cost is ${total_yearly_cost}.")
