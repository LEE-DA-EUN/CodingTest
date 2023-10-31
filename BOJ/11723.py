import sys
input = sys.stdin.readline
t = int(input())
S = set()
for _ in range(t):
    ans = list(input().split())
    if len(ans) == 1:
        if ans[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif ans[0] == 'empty':
            S = set()
    else:
        do, num = ans[0], int(ans[1])
        if do == 'add':
            if num not in S:
                S.add(num)
        elif do == 'remove':
            if num in S:
                S.remove(num)
        elif do == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif do == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.add(num)