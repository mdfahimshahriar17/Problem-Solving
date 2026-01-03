def find_even_number():
    number = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in number:
        if i%2 == 0:
            print(i)


def even_number():
    for i in range(1, 12+1): # I start count from 0 so in range function must have to declear starting point. range function don't count last index 
        if i%2 == 0:
            print(i)





find_even_number()
even_number()            
