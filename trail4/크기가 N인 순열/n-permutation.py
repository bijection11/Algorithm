n = int(input())
checked = [0] * (n+1)
picked = []

def permutation(cnt):
    if cnt == n: 
        print(*picked)
    
    for i in range(1,n+1):
        
        if checked[i]:
            continue
        checked[i] = 1 
        picked.append(i)
        permutation(1+cnt)
        checked[i] = 0
        picked.pop()

permutation(0)






