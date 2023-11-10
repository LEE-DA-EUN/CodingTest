while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        ls = [a,b,c]
        len_ls = list(set(ls))
        if max(ls) >= sum(ls) - max(ls):
            print('Invalid')
        elif len(len_ls) == 1:
            print('Equilateral')
        elif len(len_ls) == 2:
            print('Isosceles')
        else:
            print('Scalene')