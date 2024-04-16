import sys
input = sys.stdin.readline
from heapq import*

INF = sys.maxsize
t = int(input())

def dijkstra(c, graph, hack):
  q = []
  heappush(q, (0, c))
  hack[c] = 0

  while q:
    time, now = heappop(q)

    if hack[now] < time: 
      continue
    
    for i in graph[now]:
      cost = time + i[1]
      if cost < hack[i[0]]:
        hack[i[0]] = cost
        heappush(q, (cost, i[0]))


for _ in range(t):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    hack = [INF] * (n+1)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    dijkstra(c, graph, hack)

    last = 0
    count = 0
    for i in range(len(hack)):
        if hack[i] != INF:
            if hack[i] > last:
                last = hack[i]
            count += 1
    
    print(count, last)