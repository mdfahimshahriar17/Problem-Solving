def even_and_odd_count(nums):
    even_count = 0
    odd_count = 0

    for n in nums:
        if n%2 == 0:
            even_count += 1

        if n%2 != 0:
            odd_count += 1

    return even_count, odd_count

n = list(map(int, input().split()))
result = even_and_odd_count(nums=n)
print(result)