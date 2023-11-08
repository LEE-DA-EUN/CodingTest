#2503
from itertools import permutations
num = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
n = int(input())


for _ in range(n):
    check, s, b = map(int, input().split())
    check = list(str(check))
    rm_cnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rm_cnt
        for j in range(3):
            if num[i][j] == check[j]:
                strike += 1
            elif check[j] in num[i]:
                ball += 1
        if (strike != s) or (ball != b):
            num.remove(num[i])
            rm_cnt += 1
print((len(num)))
