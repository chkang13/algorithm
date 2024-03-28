from itertools import combinations

N,M = map(int, input().split())
nums = [i for i in range(1,N+1)]
perm = list(combinations(nums,M))

for i in perm:
    print(*i)
