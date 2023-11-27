n, m = map(int, input().split())
ls = [0 for i in range(n)]
for _ in range(m):
    i, j, k = map(int,input().split())
    for x in range(i, j+1):
        ls[x-1] = k
print(*ls)
