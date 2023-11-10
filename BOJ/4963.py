while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    MAX = 51
    visited = [[False for j in range(MAX)] for i in range(MAX)]
    dy = [-1,-1,0,1,1,1,0,-1]
    dx = [0,-1,-1,-1,0,1,1,1]
    arr = []
    ans = 0
    for _ in range(H):
        arr.append(list(map(int, input().split())))

    for h in range(H):
        for w in range(W):
            # 바다이거나 방문한 육지일때
            if arr[h][w] == 0 or visited[h][w]:
                continue

            # 처음 방문한 육지일때
            ans += 1
            q = []
            q.append([h,w])
            visited[h][w] = True

            while len(q) != 0:
                y = q[0][0]
                x = q[0][1]
                q.pop(0)
                for d in range(8):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= H or nx < 0 or nx >= W:
                        continue
                    if visited[ny][nx] or arr[ny][nx] == 0:
                        continue
                    visited[ny][nx] = True
                    q.append([ny, nx])
    print(ans)