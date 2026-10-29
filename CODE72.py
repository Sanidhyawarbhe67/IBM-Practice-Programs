start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    prime = True

    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False

    if prime:
        print(num)