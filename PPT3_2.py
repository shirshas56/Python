num = input("Enter a 10-digit number: ")
max_digit = '0'  
for digit in num:
    if digit > max_digit:
        max_digit = digit
print(f"The digit with the maximum value is: {max_digit}")
