def main(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * main(base, exponent - 1)
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = main(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
main(base, exponent)