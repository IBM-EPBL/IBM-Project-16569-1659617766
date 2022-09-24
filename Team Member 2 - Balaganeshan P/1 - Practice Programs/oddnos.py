m = int(input("Enter the First Num:"))
n = int(input("Enter the Second Num:"))

if n<m:
    m,n = n,m
else:
    while m <= n:
        if (m%2) != 0:
            print(m, end=" ")
        m+=1
        