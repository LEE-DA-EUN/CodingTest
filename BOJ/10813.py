n, m = map(int, input().split())
ls = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int,input().split())
    ls[i-1], ls[j-1] = ls[j-1], ls[i-1]
print(*ls)