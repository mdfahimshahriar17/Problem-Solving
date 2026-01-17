def frequency_counter(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1

        else:
            freq[num] += 1

    return freq

nums = [1, 2, 2, 3, 1, 4, 2]
result = frequency_counter(nums)
print(result)