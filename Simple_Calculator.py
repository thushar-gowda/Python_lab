def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Welcome to the Simple Calculator!")

while True:
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Thank you for using the calculator. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = divide(num1, num2)
            print("Result:", result)
    else:
        print("Invalid choice. Please try again.")
