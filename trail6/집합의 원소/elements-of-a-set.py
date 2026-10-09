n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]
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

for m,a,b in query:
    if m == 0:
        union(a-1,b-1)
    else:
        if find(a-1) == find(b-1):
            print(1)
        else: 
            print(0)
