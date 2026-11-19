K, N = map(int, input().split())

ans = []

def bt(cnt):
    if cnt == N:
        print(*ans)
        return

    for i in range(1, K+1):
        if len(ans) >= 2 and ans[-1] == ans[-2] == i:
            continue

        ans.append(i)
        bt(cnt+1)
        ans.pop()

bt(0)