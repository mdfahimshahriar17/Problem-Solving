def minimum_and_maximum_difference(nums):

    max = nums [0]
    min = nums [0]

    for num in nums:
        if num > max:
            max = num

        elif num < min:
            min = num

    diffrence = max - min

    return [min, max, diffrence]


nums = list(map(int, input("Enter list of num --> (Space will separate integer) : ").split()))
result = minimum_and_maximum_difference(nums)

print(f"Min = {result[0]}\nMax = {result[1]}\nDiffrence = {result[2]}")