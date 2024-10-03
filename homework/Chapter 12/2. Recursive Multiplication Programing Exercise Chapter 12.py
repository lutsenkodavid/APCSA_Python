def recursive_multiplication(x, y):
    if y == 0:
        return 0
    return x + recursive_multiplication(x, y -1)

x = int(input("Enter in your x variable: "))
y = int(input("Enter in your y variable: "))
    
result = recursive_multiplication(x, y)
print(f"The product of these two numbers is {result}")

    