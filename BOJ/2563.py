n = int(input())
ls = [[0 for i in range(101)]for _ in range(101)]
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            ls[i][j] += 1

for ii in range(101):
    for jj in range(101):
        if ls[ii][jj] >= 1:
            ans += 1
print(ans)
