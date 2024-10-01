speed = int(input("How fast is your car going? (mph): "))
hours = int(input("How many hours is it going that speed? "))

print("Hour		Distance Traveled")
print("__________________________________________")
    
for hour in range(1, hours + 1):
    distance = speed * hour
    print(hour,"		",distance," miles")