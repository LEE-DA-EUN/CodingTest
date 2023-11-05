h, w = map(int, input().split())
for _ in range(h):
    ls = list(input())
    ans = []
    cnt = -1
    for i in range(w):
        if ls[i] == 'c':
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
            else:
                cnt = -1
        ans.append(cnt)
    print(*ans)