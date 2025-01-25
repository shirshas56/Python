n = int(input("Enter the value of n: "))
if n % 2 == 1:
    print(f"The {n}th term in the series is: 0")
else:    
    position = n // 2  
    if position == 1:
        value = 6
    elif position == 2:
        value = 12
    elif position == 3:
        value = 90
    else:
        value = "Unknown for higher terms"
    print(f"The {n}th term in the series is: {value}")
