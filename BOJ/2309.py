ls = []
for _ in range(9):
    ls.append(int(input()))

out = sum(ls) - 100
for i in range(8):
    for j in range(i+1, 9):
        if ls[i] + ls[j] == out:
            ls.remove(ls[i])
            ls.remove(ls[j-1])
            break
    if len(ls) == 7:
        break
ls.sort()
for x in range(len(ls)):
    print(ls[x])