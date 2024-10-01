product = 0

while product < 100:
    number = float(input("Enter a number: "))  # Input a number
    product = number * 10                     # Multiply by 10 and assign to 'product'
    print(f"The product is: ", product)
    
    #if a user enters a value less than or equal to 0, it will still run and multiply which ever number you input by 10