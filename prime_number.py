# prime number it can divisable it self and 1 it start from 2

def find_prime_number(n):
    prime = False
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
    return prime        

result = find_prime_number(1)
if result:
    print("Prime")
else:
    print("Not Prime")


def prime_number():
    n = int(input("Enter a number: "))
    i = 2

    if n > 1:
        while i < n:
            if n%i == 0:
                print(f"{n} is not prime")
                break
            i += 1
        else:
            print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
prime_number()



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime_upto(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end='  ')

print_prime_upto(100)





num = int(input("Enter number : "))
if num < 2:
    print("Not Prime")
else:
    for n in range(2, int(num ** 0.5) + 1):
        if num%n == 0:
            print("Not Prime")
            break

    else:
        print("Prime")




