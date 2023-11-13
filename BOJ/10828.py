import sys
input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    ls = list(map(str, input().split()))
    if len(ls) == 2:
        do, num = ls[0], int(ls[1])
        if do == 'push':
            s.insert(0, num)
    else:
        do = ls[0]
        if do == 'pop':
            if len(s) > 0:
                print(s.pop(0))
            else:
                print(-1)

        elif do == 'size':
            print(len(s))

        elif do == 'empty':
            if len(s) > 0:
                print(0)
            else:
                print(1)
        elif do == 'top':
            if len(s) > 0:
                print(s[0])
            else:
                print(-1)
