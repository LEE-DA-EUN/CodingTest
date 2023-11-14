n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
ans = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]
for i in range(n):
    print(*ans[i])