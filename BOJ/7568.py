n = int(input())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))
for i in ls:
    ans = 1
    for j in ls:
        if i[0] < j[0] and i[1] < j[1]:
            ans += 1
    print(ans, end=' ')