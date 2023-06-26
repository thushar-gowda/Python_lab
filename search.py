def search_number(numbers, key):
    if key in numbers:
        return True
    else:
        return False

# Example usage
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers.append(num)

key = int(input("Enter the key number to search for: "))

if search_number(numbers, key):
    print("Key number found in the list.")
else:
    print("Key number not found in the list.")
