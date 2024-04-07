import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
colors = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    q =deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and colors[nx][ny] == colors[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))


result1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            result1 += 1

for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            result2 += 1

print(result1, result2)