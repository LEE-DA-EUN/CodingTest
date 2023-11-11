k, n = map(int, input().split())
ls = []
for _ in range(k):
    ls.append(int(input()))

low, high = 1, max(ls)
while low <= high:
    mid = (low+high)//2
    cnt = 0
    for i in range(k):
        cnt += ls[i] // mid
    if cnt >= n:
        low = mid+1
    elif cnt < n:
        high = mid-1
print(high)