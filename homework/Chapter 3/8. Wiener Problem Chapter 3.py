people = int(input('Enter number of people: '))
pp = int(input("Enter number of hot dogs: "))

buns = 8
hotdogs = 10

total = people * pp

wieners_needed = total // hotdogs
buns_needed = total // buns
left_over_wieners = total % hotdogs
left_over_buns = total % buns

print("Minimum number of packages of hot dogs needed is",wieners_needed,)
print("Minimum number of packages of hot dog buns needed is",buns_needed,)
print('Number of hot dogs left over are',left_over_wieners,)
print('Number of hot dogs buns left over are',left_over_buns,)