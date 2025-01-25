def nth_term(n):
    if n % 2 != 0:  
        k = (n + 1) // 2
        return 2 * k - 1
    else:  
        k = n // 2
        odd1 = 2 * k - 1
        odd2 = 2 * k + 1
        return int(str(odd1)[0] + str(odd2)[0])
n = int(input("Enter the nth term: "))
print(f"The {n}th term is {nth_term(n)}")
