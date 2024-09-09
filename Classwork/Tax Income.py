import math
def main ():
    income = float(input("Enter 2024 income: " ))
    print()
    
    if income <= 11600:
        tax = income * 0.1 
        bracket = '10% tax bracket'
    elif income <= 47150:
        tax = 1160 + (income - 11600) * 0.12
        bracket = '12% tax bracket'
        
    elif income <= 100525:
        tax = 1160 + 4265.88 + (income - 47151) * 0.22
        bracket = '22% tax bracket'
        
    elif income <= 191950:
        tax = 1160 + 4265.88 + 11742.28 +(income - 100525) * 0.24
        bracket = '24% tax bracket'
        
    elif income <= 243725:
        tax = 1160 + 4265.88 + 11742.28 + 21941.76 + (income - 191950) * 0.32
        bracket = '32% tax bracket'
        
    elif income <= 609350:
        tax = 1160 + 4265.88 + 11742.28 + 21941.76 + (243725 - 191951)*0.32 + (income - 243725) * 0.35
        bracket = '35% tax bracket'

    elif income > 609350:
        tax = 1160 + 4265.88 + 11742.28 + 21941.76 + (243725 - 191951)*0.32 + (609350 - 243725)*0.32 + (income - 243725) * 0.37
        bracket = '37% tax bracket'
        
    print("An income of" , income, 'places you in the' , bracket)
    print('The US Federal tax on an income of',income , 'is', tax)

        
main()
    