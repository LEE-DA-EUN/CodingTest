t = int(input())
for _ in range(t):
    N, check = map(int, input().split())
    ls = list(map(int, input().split()))
    ans = []
    num = 0
    for i in range(len(ls)):
        if i == check:
            ans.append([ls[i], 1])
        else:
            ans.append([ls[i], 0])
    while len(ans) != 0:
        if ans[0][0] < max(map(max, ans)): #다른 것보다 중요도 낮음 뒤로 보냄
            ans.append(ans.pop(0))
        else: #지금 바로 출력해도 됨
            num += 1 #출력 순서 확인을 위해 필요함
            if ans[0][1] == 1:
                print(num)
                break
            ans.pop(0)
