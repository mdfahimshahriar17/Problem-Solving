def count_frequency_with_tie(nums):
    int_list = list(map(int, nums))

    freq = {}
    high_freq = {}
    high = None


    for num in nums:
        if num not in freq:
            freq[num] = 1

        else:
            freq[num] += 1


    for key, val in freq.values():
        if high == None or val > high:
            high_freq.clear()
            high_freq.update({key, val})

    


    return freq






nums = input("Space will seperate the numbers\nEnter Numbers : ").split()
result = count_frequency_with_tie(nums)
print(result)