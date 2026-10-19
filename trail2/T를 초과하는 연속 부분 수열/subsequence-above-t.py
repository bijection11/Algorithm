n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
tmp = 0

for i in range(n):
    if arr[i] > t:
        tmp += 1
    else:
        tmp = 0

    ans = max(ans, tmp)

print(ans)