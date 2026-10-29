num = int(input("Enter a number: "))
prime = True

if num <= 1:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False

if prime:
    print("It is prime")
else:
    print("It is not prime")