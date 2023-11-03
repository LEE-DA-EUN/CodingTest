n, l = map(int, input().split())
start = 0
time = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += d - start
    start = d
    if time % (r+g) <= r:
        time += (r - (time % (r+g)))
time += l-start
print(time)