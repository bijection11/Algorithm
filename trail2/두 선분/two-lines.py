x1, x2, x3, x4 = map(int, input().split())

arr = [0] * 101

for i in range(x1,x2+1):
    arr[i] += 1
for i in range(x3,x4+1):
    arr[i] += 1 

ans = 'nonintersecting'
for i in arr:
    if i == 2: 
        ans = 'intersecting'
print(ans) 
        
