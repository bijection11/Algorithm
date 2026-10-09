n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
ans = float('inf')
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if i == j:
            continue

        tmp += (abs(i-j))*A[j-1]

    ans = min(ans, tmp)

print(ans)

        