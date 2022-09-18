start = int(input("Enter a Start Num:"))
end = int(input("Enter a End Num:"))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=" ")