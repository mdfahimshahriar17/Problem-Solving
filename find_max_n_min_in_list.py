def find_max_min(numbers):
    max_val = numbers[0]
    min_val = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
        if numbers[i] < min_val:
            min_val = numbers[i]

    return max_val, min_val


numbers = [5, 2, 9, 1, 7]
max_val, min_val = find_max_min(numbers)

print(max_val)
print(min_val)
