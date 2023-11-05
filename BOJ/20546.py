cash = int(input())
jh_cash = cash
sm_cash = cash
jh = 0
sm = 0
ls = list(map(int, input().split()))

for i in range(len(ls)):
    cnt = jh_cash//ls[i]
    if cnt > 0:
        jh += cnt
        jh_cash -= ls[i]*cnt
jh_result = jh_cash+ls[-1]*jh #준현이 계산끝

for j in range(len(ls)-3):
    if ls[j] > ls[j+1] and ls[j+1] > ls[j+2] and ls[j+2] > ls[j+3]:
        if sm_cash > ls[j+3]:
            cnt2 = sm_cash//ls[j+3]
            if cnt2 > 0:
                sm += cnt2
                sm_cash -= ls[j+3]*cnt2
    elif ls[j] < ls[j+1] and ls[j+1] < ls[j+2] and ls[j+2] < ls[j+3]:
        cnt2 = sm*ls[j+3]
        sm_cash += cnt2
        sm = 0
sm_result = sm_cash+ls[-1]*sm

if jh_result > sm_result:
    print('BNP')
elif jh_result < sm_result:
    print('TIMING')
else:
    print('SAMESAME')