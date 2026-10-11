
n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

# 가중치가 작은 간선부터 정렬
edges.sort()

parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    parent[b] = a
    return True

ans = 0
cnt = 0

for w, a, b in edges:
    if union(a, b):
        ans += w
        cnt += 1

        if cnt == n - 1:
            break

print(ans)
