# def count_frequency_with_tie(nums):
#     int_list = list(map(int, nums))

#     freq = {}
#     most_freq = {}
#     high = None


#     for num in int_list:
#         if num not in freq:
#             freq[num] = 1

#         else:
#             freq[num] += 1


#     for key, val in freq.items():
#         if high == None or val > high:
#             most_freq.clear()
#             most_freq.update({key, val})

#     ans = most_freq

#     tie = {}
#     for key, val in freq.items():
#         if val == most_freq.values():
#             tie.update({key : val})

    
#     if tie:
#         lowest = None
#         for key, val in tie.items():
#             if lowest == None or key < lowest:
#                 freq.clear()
#                 freq[key] = val

#         ans = freq
        
#     return ans





# nums = input("Space will seperate the numbers\nEnter Numbers : ").split()
# result = count_frequency_with_tie(nums)
# print(result)

