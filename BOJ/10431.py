for _ in range(int(input())):
    num = list(map(int, input().split()))
    case_num = num[0]
    ans = 0
    for i in range(1, len(num)-1):
        for j in range(i+1, len(num)):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
                ans +=1
    print(case_num, ans)