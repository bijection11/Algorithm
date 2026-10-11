k, n = map(int, input().split())

path = []

def dfs():
    if len(path) == n:
        print(*path)
        return

    for i in range(1, k + 1):
        path.append(i)
        dfs()
        path.pop()

dfs()