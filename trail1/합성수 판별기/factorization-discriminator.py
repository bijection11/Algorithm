N = int(input())

ans = 0 
for i in range(2,N):
    if N % i == 0:
        ans += 1 

if ans != 0:
    print("C")
else:
    print("N")