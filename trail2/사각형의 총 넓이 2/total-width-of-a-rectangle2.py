n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0 
grid = [[0]*201 for _ in range(201)]
for x1,y1,x2,y2 in arr:
    for i in range(x1,x2):
        for j in range(y1,y2):
            grid[i][j] += 1 

for i in range(201):
    for j in range(201):
        if grid[i][j] != 0:
            ans += 1 

print(ans)
