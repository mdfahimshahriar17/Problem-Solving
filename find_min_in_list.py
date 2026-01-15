def find_min(nums):
    min = nums[0]

    for idx in range(0, len(nums)):
        if nums [idx] < min:
            min = nums[idx]

    return min

nums = input("Enter Numbers : ").split()
result = find_min(nums)
print(result)