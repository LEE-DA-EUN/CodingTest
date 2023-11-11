t = int(input())
ls = []
for _ in range(t):
    ls.append(input())
ls = list(set(ls))
ls.sort()
ls.sort(key = len)
for i in range(len(ls)):
    print(ls[i])