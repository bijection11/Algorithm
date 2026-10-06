n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(n-2):
    for j in range(n-2):
        grab = 0 
        for k in range(3):
            for l in range(3):
                grab += grid[i+k][j+l] 
        
        ans = max(grab,ans)

print(ans)