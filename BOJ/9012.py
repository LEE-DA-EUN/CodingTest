n = int(input())

for _ in range(n):
    ans = []
    ls = list(input())
    for i in range(len(ls)):
        if ls[i] == '(':
            ans.append(ls[i])
        if ls[i] == ')':
            if len(ans) == 0:
                print('NO')
                break
            else:
                ans.pop()
    else:
        if len(ans) != 0:
            print('NO')
        else:
            print('YES')