ls = []
for _ in range(5):
    ls.append(list(input()))
for j in range(15):
    for i in range(5):
        if j < len(ls[i]):
            print(ls[i][j], end='')