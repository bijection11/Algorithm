a, b, c = map(int, input().split())
ans = 0 
for i in range(a,b+1):
    if i % c == 0:
        print('NO')
        ans = 1
        break

if ans == 0: 
    print("YES")

