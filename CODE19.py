a = float(input("Enter the first number: "))
op = input("Enter +, -, * or /: ")
b = float(input("Enter the second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Can't divide by zero")
    else:
        print(a / b)
else:
    print("That operation is not supported")