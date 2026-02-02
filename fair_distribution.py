def additional_chocolates():
    x, y = map(int, input().split())
    if y % x == 0:
        print(0)
    else:
        print(x - (y % x))

additional_chocolates()