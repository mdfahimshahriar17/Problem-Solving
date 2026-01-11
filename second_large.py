def find_second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            if largest != num:
                second = largest
            largest = num

        elif num != largest and (second is None or num > second):
            second = num

    return second


numbers = [10, 5, 8, 20, 15]
print(find_second_largest(numbers))
