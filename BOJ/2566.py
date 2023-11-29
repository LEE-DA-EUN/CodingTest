ls = []
for i in range(9):
    ls.append(list(map(int, input().split())))
num = max(map(max, ls))
print(num)
for i in range(9):
    for j in range(9):
        if ls[i][j] == num:
            print(i+1, j+1)
            break