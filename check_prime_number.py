"""Prime number is devisable with it self and 1 it has to be >1"""
'''Check the given number is prime or not'''

n = int(input("Enter the number : "))

if n > 1:
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    
    else:
        print("Not Prime")
else: 
    print("The Given number is not prime")