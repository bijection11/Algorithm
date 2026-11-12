from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*n for _ in range(n)]

ans = -1
di = [-2,-1,1,2,2,1,-1,-2]
dj = [1,2,2,1,-1,-2,-2,-1]

q = deque([(r1-1,c1-1)])

while q:
    i,j = q.popleft()
    if (i == r2-1) and (j == c2-1):
        ans = visited[i][j]
        break
    
    for d in range(8):
        ni = di[d] + i 
        nj = dj[d] + j
        if 0 <= ni < n and 0 <= nj < n:
            if visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1 
                
print(ans)