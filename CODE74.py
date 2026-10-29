num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original >= 0 and original == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")