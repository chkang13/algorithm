from collections import deque
import sys
input = sys.stdin.readline

count = 0 
def dfs(v):
    visited[v] = True
    global count
    count += 1
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

n = int(input())
m = int(input())
visited = [False] * (n+1)

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(count-1)