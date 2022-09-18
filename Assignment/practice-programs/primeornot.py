num = int(input("Enter a Number:"))
prime = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = True
            break
if prime:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")