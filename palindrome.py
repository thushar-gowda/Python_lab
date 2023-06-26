def is_palindrome(input):
    # Convert input to string for string palindrome check
    input_str = str(input)
    
    # Reverse the input string
    reversed_str = input_str[::-1]
    
    # Compare the original and reversed strings
    if input_str == reversed_str:
        return True
    else:
        return False

# Example usage with an integer
num = int(input("Enter an integer: "))
if is_palindrome(num):
    print("The integer is a palindrome.")
else:
    print("The integer is not a palindrome.")

# Example usage with a string
text = input("Enter a string: ")
if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
