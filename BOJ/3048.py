n1, n2 = map(int, input().split())
goright = list(input())
goright.reverse()
goleft = list(input())
t = int(input())
ready = goright + goleft
for _ in range(t):
    for i in range(len(ready)-1):
        if ready[i] in goright and ready[i+1] in goleft:
            ready[i], ready[i+1] = ready[i+1], ready[i]
            if ready[i+1] == goright[-1]:
                break
print(''.join(ready))