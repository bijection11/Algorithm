n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n-2):
        tmp = 0
        for k in range(j,j+3):
            if grid[i][k] == 1:
                tmp += 1 
        ans = max(tmp, ans)

print(ans)