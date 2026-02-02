def count_tokushuna_strings():
    t = int(input())
    for case in range(1, t + 1):
        s = input().strip()
        n = len(s)
        count = 0

        for i in range(n):
            if s[i] == '1':
                for j in range(i + 2, n):
                    if s[j] == '1':
                        ok = True
                        for k in range(i + 1, j):
                            if s[k] != '0':
                                ok = False
                                break
                        if ok:
                            count += 1

        print(f"Case {case}: {count}")

count_tokushuna_strings()
