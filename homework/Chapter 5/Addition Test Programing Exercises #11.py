import random

for x in range(1,6):
    print(f"Question #{x}")
    num1= random.randint(1, 10)
    num2= random.randint(1, 10)
    
    total = num1 + num2
    
    print(f"  {num1}")
    print(f"+ {num2}")
    
    answer = int(input("Enter the answer: "))
    
    if answer == total:
        print("CORRECT!")
        
    else:
        print("INCORRECT!")
