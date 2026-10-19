n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

ans = -1 
a = 0 
b = 0 
arr_a = []
arr_b = []

for i in range(n):
    if d[i] == 'R':
        for j in range(a+1,a+t[i]+1):
            arr_a.append(j)
        a = a + t[i]
    else:
        for j in range(a-1,a-t[i]-1,-1):
            arr_a.append(j)
        a = a - t[i]
        
for i in range(m):
    if d2[i] == 'R':
        for j in range(b+1,b+t2[i]+1):
            arr_b.append(j)
        b = b + t2[i]
    else:
        for j in range(b-1,b-t2[i]-1,-1):
            arr_b.append(j)
        b = b - t2[i]
        
for i in range(len(arr_a)):
    if arr_a[i] == arr_b[i]:
        ans = i+1
        break
print(ans)
