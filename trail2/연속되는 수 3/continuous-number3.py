N = int(input())
arr = [int(input()) for _ in range(N)]



ans = 1
tmp = 1 
for i in range(N-1):
    if arr[i] > 0 and arr[i+1] > 0:
        tmp += 1 
    elif arr[i] < 0 and arr[i+1] < 0:
        tmp += 1 
    else: 
        tmp = 1 
    ans = max(ans, tmp)

print(ans)
        