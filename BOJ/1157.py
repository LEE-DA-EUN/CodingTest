input = list(input().upper())
arr = list(set(input))
cnt = []

for i in arr:
    num = input.count(i)
    cnt.append(num)

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(arr[cnt.index(max(cnt))])
