import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

def bfs(v):
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()

        if v == k:
            return locate[v]

        for i in [v-1, v+1, 2*v]:
            if 0 <= i < 100001 and locate[i] == 0:
                locate[i] = locate[v] + 1
                q.append(i)

locate = [0] * 100001

print(bfs(n))