from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        i, j = q.popleft()

        if i == n-1 and j == m-1:
            return 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < n and 0 <= nj < m:
                if a[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))

    return 0

print(bfs())