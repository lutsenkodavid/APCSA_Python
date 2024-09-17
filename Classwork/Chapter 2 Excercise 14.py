P = float(input('Enter the amount of money which was originally desposited into the account:'))
r = float(input('Enter the annual interest rate in percent:'))
n = float(input('Enter the amount of times per year that the interest is compounded:'))
t = float(input('Enter the specified number of year'))

r /=100

A = P * ((1 + (r/n)) ** (n * t))

print('The amount of money in the account after', t, 'is:', A) 