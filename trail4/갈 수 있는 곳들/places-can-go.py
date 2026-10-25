from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[0] * n for _ in range(n)]

ans = 0

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for a, b in points:
    if visited[a-1][b-1] == 1:
        continue

    q = deque([(a-1, b-1)])
    visited[a-1][b-1] = 1
    ans += 1

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    ans += 1

print(ans)