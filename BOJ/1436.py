ls = []
i = 0
while len(ls) != 10000:
    num = list(str(i))
    if num.count('6') >= 3:
        check = 0
        for j in range(len(num)-2):
            if num[j] == '6' and num[j+1] == '6' and num[j+2] == '6':
                check = 1
        if check == 1:
            ls.append(i)
    i += 1
print(ls[int(input())-1])