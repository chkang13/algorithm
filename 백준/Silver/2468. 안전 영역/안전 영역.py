import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
safe = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y,h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > h and not visited[nx][ny]:
            dfs(nx,ny,h)

for h in range(max(map(max, graph))):
    count = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                dfs(i,j,h)
                count += 1
    safe.append(count)            
print(max(safe))