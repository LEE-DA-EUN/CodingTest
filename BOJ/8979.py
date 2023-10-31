n, k = map(int, input().split())
result = []
for _ in range(n):
    result.append(list(map(int, input().split())))
result.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if result[i][0] == k:
        index = i
for j in range(n):
    if result[index][1:] == result[j][1:]:
        print(j+1)
        break
