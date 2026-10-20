N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(M)]

A = []
a = 0
B = []
b = 0
ans = 0

for v,t in arr:
    for i in range(t):
        a += v
        A.append(a)

for v,t in arr2:
    for i in range(t):
        b += v
        B.append(b)

tmp = 0 
for i in range(len(A)):
    if A[i] > B[i]:
        if tmp == 2:
            ans += 1
        tmp = 1 
    elif B[i] > A[i]:
        if tmp == 1:
            ans += 1 
        tmp = 2
        
print(ans)

        
        


