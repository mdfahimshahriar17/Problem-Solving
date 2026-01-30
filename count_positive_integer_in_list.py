def count_positive_integer(nums):
    count = 0

    for num in nums:
        if int(num) > 0:
            count += 1

    return count

nums = input("Input numbers : ").split()
result = count_positive_integer(nums)
print(result)





def count_positive_integer(nums):
    count = 0

    for n in nums:
        if n > 0:
            count += 1

    return count

n = list(map(int, input().split()))
result = count_positive_integer(nums=n)
print(result)