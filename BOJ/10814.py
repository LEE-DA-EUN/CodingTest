n = int(input())
ls = []
for _ in range(n):
    tmp = list(map(str, input().split()))
    ls.append([int(tmp[0]), tmp[1]])
ls.sort(key = lambda x : x[0])
for i in range(n):
    print(ls[i][0], ls[i][1])