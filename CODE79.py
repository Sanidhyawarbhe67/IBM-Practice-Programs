num = int(input("Enter a number: "))
total = 0

for i in range(1, num):
    if num > 0 and num % i == 0:
        total = total + i

if num > 0 and total == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")