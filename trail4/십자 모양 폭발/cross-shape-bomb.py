n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 폭탄 폭발
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

a = grid[r-1][c-1]

for d in range(4):
    for k in range(a):
        ni = (r-1) + di[d] * k
        nj = (c-1) + dj[d] * k

        if 0 <= ni < n and 0 <= nj < n:
            grid[ni][nj] = 0

# 중력
for j in range(n):
    temp = []

    for i in range(n):
        if grid[i][j] != 0:
            temp.append(grid[i][j])

    for i in range(n):
        grid[i][j] = 0

    for i in range(len(temp)):
        grid[n-len(temp)+i][j] = temp[i]

# 출력
for row in grid:
    print(*row)