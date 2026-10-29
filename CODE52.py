nums = [2, 5, 8, 3, 10]
remove_num = int(input("What number do you want to remove? "))

if remove_num in nums:
    nums.remove(remove_num)
    print(nums)
else:
    print("That number is not in the list")