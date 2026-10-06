n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited =[[0]*m for _ in range(n)]

# 우 하 
di = [0,1]
dj = [1,0]

ans = 0
start = (0,0)
stack =[start]

while stack:
    i,j = stack.pop()
    if i == n-1 and j == m-1:
        ans = 1
        break
    visited[i][j] = 1 
    for d in range(2):
        ni = di[d] + i 
        nj = dj[d] + j
        if 0 <= ni < n and 0 <= nj < m:
            if grid[ni][nj] == 1 and visited[ni][nj] == 0:
                stack.append((ni,nj))
print(ans)
