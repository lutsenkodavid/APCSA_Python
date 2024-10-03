def main():
    lst = []
    num_elements = int(input("How many elements do you want to list? "))
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        lst.append(value)
        
    largest_value = big(lst)
    print(f"The largest value is {largest_value}")
    
def big(list):
    if len(list) == 1:
        return list[0]
    else:
        largest = big(list[1:])  # recursive step
        if list[0] > largest:
            return list[0]
        else:
            return largest
main()