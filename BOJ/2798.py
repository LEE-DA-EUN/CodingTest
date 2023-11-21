from itertools import combinations
n,m = map(int, input().split())
ls = list(map(int, input().split()))
ans = []
for i in combinations(ls, 3):
    if sum(i) <= m:
        ans.append(sum(i))
print(max(ans))
