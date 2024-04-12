import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 도시부터 시작
distance = [INF] * (n+1) # 최소 비용 저장 배열
for _ in range(m): # 그래프 생성
  u, v, w = map(int, input().split()) # u: 출발 도시, v: 도착 도시, w: 비용
  graph[u].append((v, w))

start, end = map(int, input().split()) # 출발 도시, 도착 도시

def dijkstra(start):
  q = []
  # 시작노드
  heapq.heappush(q, (0, start)) # (비용, 도시)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 가장 비용이 적게 걸리는 도시

    if distance[now] < dist: 
      continue
    
    for i in graph[now]:     # 연결된 모든 도시 탐색
      cost = dist + i[1]
      if cost < distance[i[0]]: # 기존 경로 보다 비용이 적게 든다면
        distance[i[0]] = cost # 최소 비용 저장 배열 갱신
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])