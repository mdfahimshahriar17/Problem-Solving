def count_frequency(numbers):
    
    freq = {}

    for num in numbers:
        if num not in freq:
            freq[num] = 1        
        else:
            freq[num] += 1       
    
    return freq


numbers = [1, 2, 2, 3, 1, 4]
result = count_frequency(numbers)
print(result)



    
