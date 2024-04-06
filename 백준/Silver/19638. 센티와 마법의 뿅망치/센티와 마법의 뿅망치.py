import sys
input = sys.stdin.readline
from heapq import*

n, h, t = map(int, input().split())

giant = [] 

# 최대 힙으로 변경
for i in range(n):
    heappush(giant, -int(input()))

count = 0
for _ in range(t):
    if -giant[0] < h or -giant[0] == 1:
        break
    else: # 최대 거인이 센티보다 크거나 같으면
        height = -giant[0] // 2
        heappop(giant)
        heappush(giant, -height) # 반으로 줄여서 다시 넣음
        count += 1

if -giant[0] >= h:
    print('NO')
    print(-giant[0])
else : # 센티가 가장 클 경우
    print('YES')
    print(count)
