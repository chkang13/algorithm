from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    chess[x][y] = 1

    while q:
        x,y = q.popleft()

        if x == x_end and y == y_end:
            return chess[x][y] - 1
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx,ny))

for _ in range(t):
    I = int(input())
    x_start, y_start = map(int, input().split())
    x_end, y_end = map(int, input().split())
    chess = [[0] * I for _ in range(I)]
    print(bfs(x_start,y_start))