def even_odd_split(nums):
    even_list = []
    odd_list = []

    for num in nums:
        if num%2 == 0:
            even_list.append(num)

        else:
            odd_list.append(num)

    return even_list, odd_list









nums = list(range(1, 11))
even_list, odd_list = even_odd_split(nums)

print(f"Even --> {even_list}\nOdd  --> {odd_list}")