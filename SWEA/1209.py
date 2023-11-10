size = 100

for _ in range(1,11):
    t = int(input())
    ls = []
    ans = []

    for i in range(size):
        check = list(map(int, input().split()))
        ls.append(check)

    # 각 행의 값
    for i in range(size):
        num = 0
        for j in range(size):
            num += ls[i][j]
        ans.append(num)

    #각 열의 값
    for i in range(size):
        num = 0
        for j in range(size):
            num += ls[j][i]
        ans.append(num)


    #대각선1
    num = 0
    for a in range(size):
        num += ls[a][a]
    ans.append(num)

    #대각선2
    num = 0
    for a in range(size):
        num += ls[a][size-1-a]
    ans.append(num)

    print(f"#{t} {max(ans)}")



