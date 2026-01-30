n = int(input("Enter N for : ")) #defined N for calculate
sum = 0 #defined a variable  for hold the sum
i = 0 #Defined i for counting Loop

while i <= n:
    
    sum = sum + i #Update the running total

    i += 1 # increment i by 1

print(sum)

# Sum of N without loop
n = int(input("Enter N TO Get Sum From 'ZERO' : "))

sum_result = sum(range(0, n+1)) # if we input 10 it will sum until 9
                                # That why I used n+1 
print(sum_result)




num = int(input("Enter Number : "))

total_sum = 0
for n in range(1, num+1):
    total_sum += n

print(total_sum)
