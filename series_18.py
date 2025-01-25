n = int(input("Enter the value of n: "))
char = 'a'
count = 1
index = 1
while index < n:
    char = chr(ord(char) + 1) 
    index += count 
    count += 1  
print(f"The {n}th term in the series is: {char}")
