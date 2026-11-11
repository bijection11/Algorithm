n = int(input())
a = list(map(int, input().split()))

ans = a[0]
tmp = a[0]

for i in range(1, n):
    tmp = max(a[i], tmp + a[i])
    ans = max(ans, tmp)

print(ans)