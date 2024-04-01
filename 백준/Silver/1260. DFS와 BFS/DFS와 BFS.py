from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    # 인접노드 방문 순서가 정점번호가 작은 것 부터
    # 문제에 따라 달라질 수 있음
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = True
    # 큐가 빌 때까지
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i] == 1:
                q.append(i)
                visited_bfs[i] = True


# 정점이 1부터 시작하는 것 주의
n,m,v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

# 간선 양방향 연결
for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(v)
print()
bfs(v)
