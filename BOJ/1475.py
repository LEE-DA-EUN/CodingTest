n = list(input())
ans = [0] * 10
for i in n:
    num = int(i)
    if num == 6:
        ans[9] += 1
    else:
        ans[num] += 1

ans[9] = (ans[9]+1)//2
print(max(ans))
