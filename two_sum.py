n = int(input())
arr = list(map(int, input().split()))
target = int(input())

found = False

for j in range(n):          # j goes 0,1,2... (smallest j first)
    for i in range(j):      # i is always < j
        if arr[i] + arr[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break

if not found:
    print(-1)
