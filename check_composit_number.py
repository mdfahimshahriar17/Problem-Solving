"""Composite number has more than 2 factors"""
'''composite number start from 4'''
'''Check the given number is Composite or not'''

n = int(input("Enter the number : "))

if n > 3:
    is_composite = True
    for i in range(4, n+1):
        if n%i != 0:
            is_composite = False
            break
    if is_composite:
        print("Composite")
    
    else:
        print("Not Composite")
else: 
    print("The Given number is not Composite")