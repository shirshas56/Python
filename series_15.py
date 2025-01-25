n = int(input("Enter the value of n: "))
factorial = 1
result = 1
for i in range(1, n):
    factorial *= i
result = n**3 * factorial
print(f"The {n}th term is {result}")
