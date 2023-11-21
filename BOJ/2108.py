import sys
input=sys.stdin.readline

n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
ls.sort()
print(round(sum(ls)/n))
print(ls[n//2])

cnt = {}
for i in ls:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

ans = []
for i in cnt:
    if cnt[i] == max(cnt.values()):
        ans.append(i)


if len(ans) == 1:
    print(ans[0])
else:
    print(ans[1])

print(max(ls) - min(ls))
