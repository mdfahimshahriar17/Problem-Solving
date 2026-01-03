# Perfect number holo emon ekta number, jar sob chhoto divisor gulo jog korle abar exact oi number-ta-i hoy.

def perfect_number():
    n = int(input("Enter a number : "))
    sum = 0

    for i in range(1, n):
        if n%i == 0:
            sum += i

    if sum == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not perfect number")

perfect_number()