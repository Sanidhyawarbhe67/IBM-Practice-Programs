nums = [3, 7, 2, 9, 4]
biggest = nums[0]

for num in nums:
    if num > biggest:
        biggest = num

print("The largest number is", biggest)