n = int(input("Enter the value of n: "))
result = 1
for i in range(1, n):
    result *= i
print(f"The {n}th term is {result}")
