# File: Python Karatsuba.py
# Student: David Lutsenko
#
# Date: 12 September 2024
# Description of Program: This program carries out the Karatsuba multiplication algorithm to calculate the product of two 4-digit integers.
# Github: <lutsenkodavid>
 



n1 = float(input('Enter a four digit number: '))
n2 = float(input('Enter a four digit number: '))

a = n1 // 100
b = n1 % 100

c = n2 // 100
d = n2 % 100

e = a * c

f = b * d

g = (a+b) * (c+d)

h = g - (e+f)

i = e * 10000

j = h * 100

k = i + j + f

print('Computed Product: ', k)

answer = n1 * n2

print('Expected Product: ', answer)