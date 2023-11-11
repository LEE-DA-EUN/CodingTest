import sys
sys.setrecursionlimit(10 ** 6)

dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y):
    visited[x][y] = True
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if visited[nx][ny] or arr[nx][ny] == 0:
            continue
        dfs(nx, ny)

while True:
    W, H = map(int, input().split())
    if W == H == 0:
        break
    ans = 0
    MAX = 51
    visited = [[False for j in range(MAX)] for i in range(MAX)]
    arr = []
    for h in range(H):
        arr.append(list(map(int, input().split())))

    for h in range(H):
        for w in range(W):
            # 바다인 경우, 이미 본 육지인 경우
            if arr[h][w] == 0 or visited[h][w]:
                continue
            #처음 본 육지인 경우
            ans += 1
            dfs(h, w)
    print(ans)