


def remove_duplicates(numbers):
    new_numbers = []
    for num in numbers:
        if num not in new_numbers:
            new_numbers.append(num)
    
    return new_numbers



numbers = [1, 2, 2, 3, 1, 4]
result = remove_duplicates(numbers)
print(result)   # [1, 2, 3, 4]
