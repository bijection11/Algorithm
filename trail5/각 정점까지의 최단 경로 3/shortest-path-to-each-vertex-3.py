import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]

for a, b, w in edges:
    graph[a].append((b, w))

INF = float('inf')
dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    cost, now = heapq.heappop(pq)

    if cost > dist[now]:
        continue

    for nxt, weight in graph[now]:
        new_cost = cost + weight

        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

for i in range(2, n + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])