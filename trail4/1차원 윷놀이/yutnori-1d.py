n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

now = [1] * k 
ans = 0 

def backtracking(turn):
    global ans
    
    if turn == n:
        score = 0 
        for p in now:
            if p >= m:
                score += 1 
        ans = max(ans, score)
        return

    for i in range(k):
        now[i] += nums[turn]
        backtracking(turn + 1)
        now[i] -= nums[turn]

backtracking(0)
print(ans)