n = int(input())
arr = [int(input()) for _ in range(n)]

ans = 1
tmp = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        tmp += 1 
    else: 
        tmp = 1
    ans = max(tmp,ans)


print(ans)