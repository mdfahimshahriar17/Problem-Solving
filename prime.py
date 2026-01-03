def check_prime(n):
    if n < 2:
        return f"The given number is not Prime"
    else:
        for i in range(2, n):
            if n % i == 0:
                return f"The given number is not Prime"
            
    return f"The given number is prime"
result = check_prime(7)
print(result)
