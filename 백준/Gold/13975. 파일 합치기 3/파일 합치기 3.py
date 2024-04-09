import sys
input = sys.stdin.readline
from heapq import *

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    cost = 0

    while len(files) > 1:
        file1 = heappop(files)
        file2 = heappop(files)
        cost += file1 + file2

        heappush(files, file1 + file2)

    print(cost)