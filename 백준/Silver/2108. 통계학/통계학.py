import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

# 산술평균 
print(round(sum(nums) / len(nums)))

# 중앙값
print(nums[len(nums) // 2])

# 최빈값
dic = Counter(nums)

count = max(dic.values()) # 최다 빈도수
max_count  = [] # 최빈값들 저장 배열
for i in dic:
    if dic[i] == count:
        max_count.append(i)

max_count.sort()
if len(max_count) > 1:
    print(max_count[1]) # 두번째로 작은 값
else:
    print(max_count[0])

# 범위
print(max(nums) - min(nums))