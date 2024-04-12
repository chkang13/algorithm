import sys
input = sys.stdin.readline
from heapq import *

INF = 1e8

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dijkstra():
  q = []
  # 시작노드
  heappush(q, (graph[0][0],0,0)) # (비용, x좌표, y좌표)
  distance[0][0] = 0

  while q:
    black, x, y = heappop(q) # 가장 비용이 적게 걸리는 도시

    if x == n-1 and y == n-1: # 동굴의 끝에 도착하면 
        print(f'Problem {count}: {distance[x][y]}')
        break
    
    for i in range(4): # 인접한 길
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n: # 갈 수 있는 길이고
            rupee = black + graph[nx][ny]
            
            if rupee < distance[nx][ny]: # 최소 비용 저장 배열 갱신
                distance[nx][ny] = rupee
                heappush(q, (rupee, nx, ny))


count = 1
while True:
    n = int(input())
    if n == 0:
       break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)] # 최소 비용 저장 배열

    dijkstra()
    count += 1