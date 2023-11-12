import sys
input = sys.stdin.readline
n = int(input())
q = []
for i in range(n):
    ls = list(map(str, input().split()))
    if len(ls) == 2:
        do, num = ls[0], int(ls[1])
        if do == 'push':
            q.append(num)
    else:
        do = ls[0]
        if do == 'pop':
            if len(q) > 0:
                print(q.pop(0))
            else:
                print(-1)

        elif do == 'size':
            print(len(q))

        elif do == 'empty':
            if len(q) > 0:
                print(0)
            else:
                print(1)

        elif do == 'front':
            if len(q) > 0:
                print(q[0])
            else:
                print(-1)

        elif do == 'back':
            if len(q) > 0:
                print(q[-1])
            else:
                print(-1)