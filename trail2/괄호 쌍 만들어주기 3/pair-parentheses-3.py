A = input()

ans = 0
for i in range(len(A)):
    if A[i] == '(':
        for j in range(i,len(A)):
            if A[j] == ')':
                ans += 1 

print(ans)
