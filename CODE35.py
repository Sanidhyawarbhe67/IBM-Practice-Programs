n = int(input("How many numbers will you enter? "))

if n <= 0:
    print("Enter at least one number")
else:
    biggest = int(input("Enter a number: "))

    for i in range(1, n):
        num = int(input("Enter a number: "))

        if num > biggest:
            biggest = num

    print("The largest number is", biggest)