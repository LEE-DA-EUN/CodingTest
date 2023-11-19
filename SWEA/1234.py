for t in range(1, 11):
    n, ls = map(int, input().split())
    ls = list(str(ls))
    ans = []
    for i in ls:
        if len(ans) == 0:
            ans.append(i)
        else:
            if ans[-1] == i:
                ans.pop()
            else:
                ans.append(i)
    ans = ''.join(ans)
    print(f'#{t} {int(ans)}')