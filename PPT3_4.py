even_num=[]
for i in range(1000,3001):
    num_str=str(i)
    if int(num_str[0]) % 2 == 0 and int(num_str[1]) % 2 == 0 and int(num_str[2]) % 2 == 0 and int(num_str[3]) % 2 == 0:
        even_num .append(i)
print(even_num)
