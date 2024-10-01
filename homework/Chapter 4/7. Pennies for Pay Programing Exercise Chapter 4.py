days = int(input("Enter the number of days: "))
total = 0
for i in range(days):
    pay = 2 ** i
    total += pay
    print(i+1, "	",pay)
total_pay = total / 100
print('The total pay at the end of the period was', total_pay,)