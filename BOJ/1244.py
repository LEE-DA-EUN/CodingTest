s = int(input()) #스위치 개수
ls = list(map(int, input().split())) # 1 = 켜져있음 / 0 = 꺼져있음
students = int(input()) #학생수
stu_ls = []
for i in range(students):
    stu_ls.append(list(map(int, input().split()))) # 1 = 남학생 / 2 = 여학생

for i in range(students):

    # 남학생인 경우, 배수의 상태를 바꾼다
    if stu_ls[i][0] == 1:
        num = stu_ls[i][1]
        for j in range(s):
            if (j+1)%num == 0:
                if ls[j] == 1:
                    ls[j] = 0
                elif ls[j] == 0:
                    ls[j] = 1

    # 여학생인 경우, 좌우 대칭이 되는 가장 많은 범위의 상태를 모두 바꾼다
    if stu_ls[i][0] == 2:
        num = stu_ls[i][1] - 1
        change = []
        change.append(num)
        for j in range(1, s):
            left = num - j
            right = num + j
            if left < 0 or right >= s or ls[left] != ls[right]:
                break
            if ls[left] == ls[right]:
                change.append(left)
                change.append(right)

        for k in change:
            if ls[k] == 0:
                ls[k] = 1
            elif ls[k] == 1:
                ls[k] = 0

for i in range(s):
    if (i+1) % 20 == 0:
        print(ls[i])
    else:
        print(ls[i], end=' ')