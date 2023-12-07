import sys
input = sys.stdin.readline
n = int(input())
ls = []
ans = 0
for i in range(n):
    ls.append(list(map(int, input().split())))
ls.sort(key=lambda x: (x[1], x[0]))

start = 0
for i in ls:
    if start <= i[0]:
        start = i[1]
        ans += 1
print(ans)