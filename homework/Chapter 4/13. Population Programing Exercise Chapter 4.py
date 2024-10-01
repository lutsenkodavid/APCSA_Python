number = int(input("Enter the starting number of organisms: "))
increasing_percentage = int(input("Enter the average daily increase (as a percentage): "))
days = int(input("Enter the number of days: "))

print("Day Approximate 		Population")

for i in range(1, days + 1):
    print(i, "			", number,)  
    if i > 1:
        increase = number * increasing_percentage / 100
        number += increase
print(i,"			",number)