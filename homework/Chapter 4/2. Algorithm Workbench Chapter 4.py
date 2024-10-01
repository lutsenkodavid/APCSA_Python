while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = num1 + num2
    print(f"The sum of",num1," and" ,num2, "is: ",total)

    repeat = input("Do you want to perform another operation? (yes/no): ")
    if repeat == 'yes':
        continue
    else:
        print('Exiting the program.')
        break
   