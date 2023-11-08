n, m = map(int, input().split())
chess = []
ans = []
for _ in range(n):
    chess.append(str(input()))

for i in range(n-7):
    for j in range(m-7):
        num1 = 0
        num2 = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if chess[x][y] != 'W':
                        num1 += 1
                    if chess[x][y] != 'B':
                        num2 += 1
                else:
                    if chess[x][y] != 'B':
                        num1 += 1
                    if chess[x][y] != 'W':
                        num2 += 1
        ans.append(min(num1, num2))
print(min(ans))
