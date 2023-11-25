import sys
input = sys.stdin.readline
N = int(input()) #몇분
q = []
ans = 0
for i in range(N):
    ls = list(map(int, input().split()))
    if ls[0] == 1:
        q.append([ls[1], ls[2]])

    if q:
        q[-1][1] -= 1
        if q[-1][1] == 0:
            ans += q[-1][0]
            q.pop()

print(ans)