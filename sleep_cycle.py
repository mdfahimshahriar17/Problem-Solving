def calculate_bedtimes():
    t = int(input())
    for _ in range(t):
        time = input().strip()
        h, m = map(int, time.split(":"))
        wake = h * 60 + m
        base = wake - 15

        t5 = base - 450
        t6 = base - 540

        if t5 < 0:
            t5 += 1440
        if t6 < 0:
            t6 += 1440

        def fmt(t):
            return f"{t//60:02d}:{t%60:02d}"

        a, b = fmt(t5), fmt(t6)
        if a < b:
            print(a, b)
        else:
            print(b, a)

calculate_bedtimes()