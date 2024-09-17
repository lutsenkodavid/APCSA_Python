R = float(input('Enter the length of the row:'))
E = float(input('Enter the amount of space used by an end-post asssembly: '))
S = float(input('Enter the amount of space in between the vines:'))

V= (R - 2 * (E)) / S

print('The number of grapevines that will fit in the row is', V)