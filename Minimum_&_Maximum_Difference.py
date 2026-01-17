def minimum_and_maximum_difference(nums):

    max_val = nums [0]
    min_val = nums [0]

    for num in nums:
        if num > max_val:
            max_val = num

        elif num < min_val:
            min_val = num

    diffrence = max_val - min_val

    return [min_val, max_val, diffrence]


nums = list(map(int, input("Enter list of num --> (Space will separate integer) : ").split()))
result = minimum_and_maximum_difference(nums)

print(f"Min = {result[0]}\nMax = {result[1]}\nDiffrence = {result[2]}")