quantity = float(input("Enter the number of packages purchased: "))
package = 99.00

if quantity < 0:
    print("Error. The number of packages must be greater than 0")
else:
    if quantity < 10:
        discount = 0
        
    elif quantity >= 10 and quantity <=19:
        discount = .10
    
    elif quantity >= 20 and quantity <=49:
        discount = .20

    elif quantity >= 50 and quantity <=99:
        discount = .30
        
    elif quantity >= 100:
        discount = .40
        
        
    total = quantity * package
    discount_amount = total * discount
    grand_total = total - discount_amount
print("The package total is",total)
print("The disount percentage is",100*(discount),'%')
print("The discounted amount was",discount_amount)
print("The grand total amount is",grand_total)
    