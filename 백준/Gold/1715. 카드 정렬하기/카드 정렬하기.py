import sys
input = sys.stdin.readline
from heapq import *

n = int(input())

heap = []
for _ in range(n):
    card = int(input())
    heap.append(card)

heapify(heap)

compare = 0
while len(heap) > 1:
    num1 = heappop(heap)
    num2 = heappop(heap)

    compare += num1 + num2

    heappush(heap, num1 + num2 )

print(compare)