n, k = map(int, input().split())
ls = []
ans = 0
for _ in range(n):
    num = int(input())
    ls.insert(0, num)

for i in range(n):
    if k // ls[i] > 0:
        ans += k//ls[i]
        k = k % ls[i]
print(ans)