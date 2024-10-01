tuition = 8000

print("Year		Tuition")

for i in range(1,6):
    tuition += tuition * 0.03
    print(i,"		",tuition)