def nth_term(n):
    if n % 2 == 0:  
        return n // 2
    else:  
        return (n // 2) * 2
n = int(input("Enter the nth term: "))
print(f"The {n}th term is {nth_term(n)}")
