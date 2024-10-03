def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

def main():
    num_elements = int(input("Enter the amount of elements you want to list: "))
    numbers = [0]
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        numbers = numbers + [value]
        
    total = recursive_sum(numbers)
    print(f"The total sum of the elements is {total}")
main()
