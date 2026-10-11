n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        size[a] += size[b]

def count(a):
    return size[find(a)]

for _ in range(m):
    op, *nums = input().split()

    if op == "x":
        a, b = map(int, nums)
        union(a, b)
    else:
        a = int(nums[0])
        print(count(a))