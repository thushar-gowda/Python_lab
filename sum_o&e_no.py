def sum_odd_even(numbers):
    odd_sum = 0
    even_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return odd_sum, even_sum

# Example usage
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers.append(num)

odd_sum, even_sum = sum_odd_even(numbers)
print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)
