n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0 
for i in range(n-k+1):
    tmp = 0
    for j in range(k):
        tmp += arr[i+j]
    
    ans = max(ans, tmp)
print(ans)