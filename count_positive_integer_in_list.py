def count_positive_integer(nums):
    count = 0

    for num in nums:
        if num > 0:
            count += 1

    return count

list_of_nums = [-2, 3, 0, 7, -1]

result = count_positive_integer(list_of_nums)
print(result)