import sys
input = sys.stdin.readline
from heapq import *

heap = []
n = int(input())

for _ in range(n):
    num = int(input())

    if num != 0: # 0이 아닌 경우 힙에 쌍으로 넣는다
        heappush(heap, (abs(num), num))
    
    else:
        if not heap: # 힙이 비어있는 경우
            print(0)
        else:
            print(heappop(heap)[1])