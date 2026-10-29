n = int(input("Enter a number: "))
answer = 1

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        answer = answer * i

    print("The factorial is", answer)