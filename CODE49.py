nums = [2, 5, 8, 3, 10]
count = 0

for num in nums:
    if num % 2 == 0:
        count = count + 1

print("Even numbers:", count)