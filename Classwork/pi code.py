import math

def main():
    r = float(input("Enter the radius of a circle: "))
    if (r >= 0):
        area = math.pi * r ** 2
        print ('A circle with a radius of ', r,
               'has an area of ', area)
    else:
        print('Negative radius entered: ',r)
main()