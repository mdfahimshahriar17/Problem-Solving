def find_odd_number(n):
    for i in n:
        if i%2 != 0:
            print(i)
number=[1,2,3,4,5,6,7,8,9,10,11]
find_odd_number(number)

#'list' object cannot be interpreted as an integer
#during list itterat instead of range(n) we have to use i in n