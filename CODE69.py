n = int(input("How many numbers do you want? "))
a = 0
b = 1

for i in range(n):
    print(a)
    next_num = a + b
    a = b
    b = next_num