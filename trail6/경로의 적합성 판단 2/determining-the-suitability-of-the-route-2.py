n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

parent = [i for i in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

for a,b in edges:
    union(a-1,b-1)

tmp = 1
for i in range(k-1):
    if find(path[i]-1) != find(path[i+1]-1):
        tmp = 0
        break
print(tmp)

    