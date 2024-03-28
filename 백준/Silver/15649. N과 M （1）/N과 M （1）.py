from itertools import permutations

N,M = map(int, input().split())
nums = [i for i in range(1,N+1)]
perm = list(permutations(nums,M))

for i in perm:
    for j in i:
        print(j, end = ' ')
    print()