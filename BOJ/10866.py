import sys
from collections import deque
input = sys.stdin.readline
q = deque([])
for i in range(int(input())):
    ls = list(map(str, input().split()))
    if len(ls) == 2:
        do, num = ls[0], int(ls[1])
        if do == 'push_front':
            q.appendleft(num)
        elif do == 'push_back':
            q.append(num)
    else:
        do = ls[0]
        if do == 'pop_front':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif do == 'pop_back':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
        elif do == 'size':
            print(len(q))
        elif do == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif do == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif do == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])