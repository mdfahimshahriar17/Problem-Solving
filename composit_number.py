#Composit number which has more than 2 factor. it start from 4. 2, 3 is prime number

def find_composite_number(n):
    composite = False
    if n > 3:
        for i in range(2, n):
            if n % i == 0:
                composite = True
                break
    return composite        

result = find_composite_number(4)
if result:
    print("Composit")
else:
    print("Not Composit")



def composite_number():
    n = int(input("Enter a number: "))
    i = 2
    
    if n > 3:
        while i < n:
            if n%i == 0:
                print(f"{n} is Composite")
                break
            i+=1
        else:
            print(f"{n} is not composite")
    else:
        print(f"{n} is not composite")

composite_number()


def is_composite(n):
    composite = False
    if n > 3:
        for i in range(2,n):
            if n%i == 0:
                composite = True
                break
    return composite


def check_composite_upto(n):

    for num in range(2, n+1):

        if is_composite(num):
            print(num,end=' ')

check_composite_upto(20)


