num = int(input("Enter a number: "))
original = num
temp = num
digits = 0
total = 0

if temp == 0:
    digits = 1

while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")