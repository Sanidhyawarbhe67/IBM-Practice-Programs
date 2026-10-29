a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    temp = b
    b = a % b
    a = temp

print("The GCD is", a)