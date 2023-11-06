ans = [(i*(i+1))//2 for i in range(1,46)]
ls = []
for x in ans:
    for y in ans:
        for z in ans:
            num = x+y+z
            if num <= 1000:
                ls.append(num)
t = int(input())
for _ in range(t):
    check = int(input())
    if check in ls:
        print(1)
    else:
        print(0)

