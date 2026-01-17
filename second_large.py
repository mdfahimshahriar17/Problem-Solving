def find_second_largest(nums):
    
    if nums[0] > nums[1]:
        large = nums[0]
        second_large = nums[1]

    else:
        large = nums[1]
        second_large = nums[0]

    
    for num in nums:
        if num > large:
            second_large = large
            large = num

        elif num < large and num > second_large:
            second_large = num


    return large, second_large

nums = [55, 22, 33, 11, 88, 66, 44]
result = find_second_largest(nums)
print(f"Second Large -- {result[1]}\nLarge -- {result[0]}")