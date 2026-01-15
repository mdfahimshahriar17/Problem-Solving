def count_positive_integer(nums):
    count = 0

    for num in nums:
        if int(num) > 0:
            count += 1

    return count

nums = input("Input numbers : ").split()
result = count_positive_integer(nums)
print(result)