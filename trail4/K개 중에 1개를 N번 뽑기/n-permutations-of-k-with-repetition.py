k, n = map(int, input().split())

ans = []

def dfs():
    if len(ans) == n:
        print(*ans)
        return

    for i in range(1, k + 1):
        ans.append(i)
        dfs()
        ans.pop()

dfs()
