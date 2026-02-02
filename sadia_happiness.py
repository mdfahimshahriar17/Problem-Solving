def is_sadia_happy():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        avg = (x + y) / 2
        if avg % 2 == 0:
            print("Sadia will be happy.")
        else:
            print("Oops!")

is_sadia_happy()