n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))



for i in range(t):
    l.insert(0,d.pop(-1))
    r.insert(0,(l.pop(-1)))
    d.insert(0,r.pop(-1))

print(*l)
print(*r)
print(*d)