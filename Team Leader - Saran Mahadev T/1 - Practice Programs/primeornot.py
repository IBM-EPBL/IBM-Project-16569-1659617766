num = int(input("Enter a Number:"))
notprime = False
if num > 1:
    for i in range(2, num):
        if num%i == 0:
            notprime = True
            break
    if notprime:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")
else:
        print(f"{num} is not a prime number")
