def cube_number(numbers):
    cub_nums = []
    for i in numbers:
        cube = i ** 3
        
        cub_nums.append(cube)
        
    return cub_nums

numbers = [1,2,3,4,5,6,7,8,9,10]
result = cube_number(numbers)
print(result)