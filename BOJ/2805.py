n, m = map(int, input().split()) # n = 나무의 수 / m = 가져가려고 하는 나무의 길이
ls = list(map(int, input().split()))
low, high = 1, max(ls)
while low <= high:
    mid = (low+high) // 2
    cnt = 0
    for i in range(n):
        if ls[i] < mid:
            continue
        cnt += ls[i]-mid
    if cnt >= m:
        low = mid+1
    elif cnt < m:
        high = mid-1
print(high)