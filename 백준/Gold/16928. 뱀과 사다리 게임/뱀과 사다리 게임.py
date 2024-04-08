import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()

        for i in range(1,7):
            nx = x + i 

            if visited[board[nx]] == 0 and nx <= 100:
                visited[board[nx]] = visited[x] + 1

                if board[nx] == 100:
                    return visited[board[nx]]
                
                q.append(board[nx])

board = [i for i in range(101)]
visited = [0] * 101

for _ in range(n + m): # 뱀과 사다리 이동 위치 저장
    x, y = map(int, input().split())
    board[x] = y

print(bfs(1))