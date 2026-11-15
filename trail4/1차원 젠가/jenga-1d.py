n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())


blocks =  blocks[0:s1-1] + blocks[e1:]
blocks =  blocks[0:s2-1] + blocks[e2:]
print(len(blocks))
for i in blocks:
    print(i)
