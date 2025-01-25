def nth_term(n):
    if n % 2 != 0:  
        return 14 + 6 * ((n - 1) // 2)
    else:  
        return 28 + 12 * ((n // 2) - 1)
n = int(input("Enter the term you want: "))
print(f"The {n}th term is {nth_term(n)}")
