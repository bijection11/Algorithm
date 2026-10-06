n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

a = []
di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(n):
    for j in range(n):
        tmp = grid[i][j]
        
        stack = [(i,j)]
        if visited[i][j] == 1:
            continue

        visited[i][j] = 1
        cnt = 1 
        while stack:
            ci, cj = stack.pop()
            for d in range(4):
                ni = di[d] + ci
                nj = dj[d] + cj
                if 0 <= ni < n and 0 <= nj < n:
                    if visited[ni][nj] == 0 and grid[ni][nj] == tmp:
                        stack.append((ni,nj))
                        visited[ni][nj] = 1
                        cnt += 1

        a.append(cnt)
ans1 = 0
ans2 = max(a)
for i in a:
    if i >= 4:
        ans1 += 1
print(ans1, ans2)