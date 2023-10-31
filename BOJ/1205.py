n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    ls = list(map(int, input().split()))
    if score <= ls[len(ls)-1] and p == len(ls):
        print(-1)
    else:
        for i in range(len(ls)):
            ans = n+1
            if score >= ls[i]:
                ans = i+1
                break
        print(ans)
    