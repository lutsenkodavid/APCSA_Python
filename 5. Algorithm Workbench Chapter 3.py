amount1 = int(input("Please enter an integer: "))
amount2 = int(input("Please enter another integer: "))

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print("Amount number 1 is greater")
    elif amount2 > amount1:
        print("Amount number 2 is greater")
else:
    print("you are doing sumting wong")