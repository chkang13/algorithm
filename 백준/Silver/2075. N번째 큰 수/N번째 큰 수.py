import sys
input = sys.stdin.readline
from heapq import *

n = int(input())

heap = []

for i in range(n):
    # 첫 번째 행의 값들 입력
    table = list(map(int, input().split()))
    for j in range(n):
        if len(heap) < n: # 최소힙의 크기 제한
            heappush(heap, table[j])

        else:
            if heap[0] < table[j]: # 최솟값보다 현재값이 큰 경우
                heappop(heap)
                heappush(heap, table[j])

print(heap[0])