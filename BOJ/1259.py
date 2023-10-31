while(1):
    ls = list(input())
    if ls[0] == '0':
        break
    sl = list(reversed(ls))
    if ls == sl:
        print('yes')
    else:
        print('no')