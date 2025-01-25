num = input("Enter a 4-digit number: ")
even_digits = []
odd_digits = []
for digit in num:
    if int(digit) % 2 == 0:
        even_digits.append(int(digit))
    else:
        odd_digits.append(int(digit))
print("Even digits:", even_digits, "Total even digits:", len(even_digits))
print("Odd digits:", odd_digits, "Total odd digits:", len(odd_digits))
