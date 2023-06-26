def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

# Example usage
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers.append(num)

sorted_numbers = sort_numbers(numbers)
print("Sorted numbers in ascending order:", sorted_numbers)
