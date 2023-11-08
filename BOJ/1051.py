n, m = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(list(input()))

check = min(n, m)
ans = 0
for k in range(check):
    for i in range(n-k):
        for j in range(m-k):
            if ls[i][j] == ls[i][j+k] == ls[i+k][j] == ls[i+k][j+k]:
                ans = max(ans, (k+1)**2)
print(ans)

