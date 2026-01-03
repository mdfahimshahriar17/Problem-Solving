def square_number():
    number = [1,2,3,4,5,6,7,8,9,10]

    for i in number:
        #we can write it 2 way it will give same result
        square = i**i
        square = i**2

        print(square)


def square_number_in_while_loop():
    number = [1,2,3,4,5,6,7,8,9,10]

    i = 0
    while i < len(number):

        square = number[i] ** 2
        print(square)
        i += 1



square_number()
square_number_in_while_loop()