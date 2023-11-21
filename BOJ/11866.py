from collections import deque
n, k = map(int, input().split())
ls = deque([str(i) for i in range(1, n+1)])
ans = []
while len(ls) != 0:
    for i in range(k-1):
        ls.append(ls.popleft())

    ans.append(ls.popleft())

print('<'+', '.join(ans)+'>')