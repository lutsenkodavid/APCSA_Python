import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print('Radius', radius)
print('Area', area)
print('Circumference', circumference)