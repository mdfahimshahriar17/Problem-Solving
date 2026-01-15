def sum_of_digits(digits):

    sum_of_digits = 0

    for digit in digits:
        sum_of_digits += int(digit)

    return sum_of_digits

digits = input("Input the digitd : ")
digits = list(digits)

result = sum_of_digits(digits)
print(result)