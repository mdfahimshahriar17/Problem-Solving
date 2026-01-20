def find_second_largest(nums):
    
    if nums[0] > nums[1]:
        large = nums[0]
        second_large = nums[1]

    else:
        large = nums[1]
        second_large = nums[0]

    
    for num in nums[2:]:
        if num > large:
            second_large = large
            large = num

        elif num < large and num > second_large:
            second_large = num


    return large, second_large

nums = [55, 22, 33, 11, 88, 66, 44]
result = find_second_largest(nums)
print(f"Second Large -- {result[1]}\nLarge -- {result[0]}")







def second_large(nums):
    highest = None
    second_highest = None

    for num in nums:
        if highest == None or num > highest:
            second_highest = highest
            highest = num

        elif num < highest and num > second_highest:
            second_highest = num

    return highest, second_highest


nums = list(map(int, input("Space will separate the number : ").split()))
f_highest, s_highest = second_large(nums)
print(f"Highest--{f_highest}\nSecond Highest--{s_highest}")