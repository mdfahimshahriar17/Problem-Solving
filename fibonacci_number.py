# Fibonacci Numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34
# Fibonacci series holo porer number pawa jay ager 2 number jog korle
# Fibonacci series is a number sequence where each number is made by adding the two numbers before it.

def fibonacci_number():
    n = int(input("How many fibonacci numbers you want?"))
    a = 0
    b = 1

    i = 0
    while i < n:
        print(a, end=' ')
        next_number = a+b
        a = b
        b = next_number
        i += 1

fibonacci_number()
