num = int(input("Enter a number: "))
temp = num
total = 0

if temp == 0:
    total = 1

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10

if num >= 0 and total == num:
    print("It is a strong number")
else:
    print("It is not a strong number")