N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

ans = -1 
arr = [0]*N
for i in range(M):
    arr[student[i]-1] += 1
    if arr[student[i]-1] >= K:
        ans = student[i]
        break


print(ans)