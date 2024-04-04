import sys
input = sys.stdin.readline
from heapq import *

n,m = map(int, input().split())
nums = list(map(int, input().split()))
heapify(nums) # 리스트를 heap으로 변환

for _ in range(m):
    num1 = heappop(nums)
    num2 = heappop(nums)

    heappush(nums, num1 + num2)
    heappush(nums, num1 + num2)

print(sum(nums))