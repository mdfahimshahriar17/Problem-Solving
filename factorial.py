def factorial(n):
    #5! = 5 × 4 × 3 × 2 × 1
    result = 1

    while n > 0:
        result *= n
        print(result)
        n-= 1
        print(n)
    return result

x = factorial(5)
print(x)



