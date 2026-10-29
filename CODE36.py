n = int(input("How many numbers will you enter? "))

if n <= 0:
    print("Enter at least one number")
else:
    smallest = int(input("Enter a number: "))

    for i in range(1, n):
        num = int(input("Enter a number: "))

        if num < smallest:
            smallest = num

    print("The smallest number is", smallest)