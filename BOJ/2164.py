from collections import deque
n = int(input())
ls = deque([i for i in range(1, n+1)])

while len(ls) != 1:
    ls.popleft()
    ls.append(ls.popleft())
print(ls[0])