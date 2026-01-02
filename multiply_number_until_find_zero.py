n = 1 #Defined n=1 because when n = 0 mean False the current loop will be stop
result = 1  #defined the variable for hold te multiplication
            #Some times we made a mistaks here. result = 0
            #if the result = 0 the value never will multiply EX: 0*10 = 0

while n:
    n = int(input("Enter number : "))

    result = result * n

print(result)