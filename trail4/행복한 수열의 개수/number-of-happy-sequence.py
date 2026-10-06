n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# row
for i in range(n):
    cnt = 1
    if cnt >= m:
        ans += 1 
        continue
        
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            cnt += 1 
        else:
            cnt = 1
        if cnt >= m:
            ans += 1 
            break
# column
for j in range(n):
    cnt = 1
    if cnt >= m:
        ans += 1 
        continue

    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
            cnt += 1 
        else:
            cnt = 1
        if cnt >= m:
            ans += 1 
            break
print(ans)