
def even_number():
    for i in range(1, 12+1): # I start count from 0 so in range function must have to declear starting point. range function don't count last index 
        if i%2 == 0:
            print(i)

even_number()


def get_even_numbers(numbers):
    new_numbers = []

    for num in numbers:
        if num%2 == 0:

            new_numbers.append(num)
    return new_numbers
            




numbers = [1, 2, 3, 4, 5, 6]
result = get_even_numbers(numbers)
print(result)   # [2, 4, 6]

