import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
nums_sort = sorted(set(nums)) # 정렬용 배열

dic = {}

for i in range(len(nums_sort)):
    if nums_sort[i] not in dic: # 해당 키 값이 없으면
        dic[nums_sort[i]] = i # 인덱스 넣기

for i in nums:
    print(dic[i], end = ' ')