a, b, c, d = map(int, input().split())

# 2시 5분부터 116분이 흘러야 4시 1분이 됩니다.

h1 = a*60 + b 
h2 = c*60 + d 

print(h2-h1)