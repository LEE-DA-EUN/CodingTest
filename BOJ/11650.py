t = int(input())
ls = []
for _ in range(t):
    ls.append(list(map(int, input().split())))
ls.sort(key = lambda x : (x[0], x[1]))
for i in range(len(ls)):
    print(ls[i][0], ls[i][1])