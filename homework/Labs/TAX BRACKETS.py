def main():
    print('Welcome to our friendly tax computing program.')
    print('Please follow the directions.')
    
    marital_status = input('Please enter your marital status (s or m): ')
    
    if marital_status not in ['s', 'm']:
        print("Bad marital status entered! Try again later.")
        return  
    income = float(input("Enter your taxable income: "))
    
    if income < 0:
        print("Negative income reported! Try again later.")

    if marital_status == 's':
        if income <= 8000:
            tax = income * 0.10
        elif income <= 32000:
            tax = 800 + (income - 8000) * 0.15
        else:
            tax = 4400 + (income - 32000) * 0.25
        mariage = "Single"
    else:
        if income <= 16000:
            tax = income * 0.10
        elif income <= 64000:
            tax = 1600 + (income - 16000) * 0.15
        else:
            tax = 8800 + (income - 64000) * 0.25
        mariage = "Married"

    print('Marital status:',mariage)
    print('Taxable income:',income)
    print('Taxes owed:',tax)
main()