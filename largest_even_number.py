def find_largest_even(numbers):

    even_num = []
    max_even_num = 0

    for idx in range(0, len(numbers)):
        if numbers[idx]%2 == 0:
            even_num.append(numbers[idx])

            for num in even_num:
                if num > max_even_num:
                    max_even_num = num       

    if not max_even_num:
        max_even_num = None        
    return max_even_num

           
numbers = [3, 7, 2, 8, 5]
print(find_largest_even(numbers))   # 8

numbers = [1, 3, 5]
print(find_largest_even(numbers))   # None



def find_largest_even(numbers):
    max_even = None

    for num in numbers:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num

    return max_even

