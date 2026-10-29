nums = [3, 7, 2, 9, 4]
smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

print("The smallest number is", smallest)