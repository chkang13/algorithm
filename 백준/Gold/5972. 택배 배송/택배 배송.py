import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
INF = sys.maxsize

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가
cow = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split()) # a: 출발 헛간, b: 도착 헛간, c: 소 
  # 양 방향
  graph[a].append((b, c))
  graph[b].append((a, c))


def dijkstra():
  q = []
  # 시작 헛간 : 1
  heapq.heappush(q, (0, 1)) # 소, 헛간
  cow[1] = 0

  while q:
    cost, now = heapq.heappop(q) # 소가 가장 적은 길

    if cow[now] < cost: 
      continue
    
    for i in graph[now]:     # 연결된 모든 노드 탐색
      food = cost + i[1]
      if food < cow[i[0]]: # 기존에 입력되어있는 값보다 작다면
        cow[i[0]] = food # 가중치 배열 갱신
        heapq.heappush(q, (food, i[0]))

dijkstra()

print(cow[n])