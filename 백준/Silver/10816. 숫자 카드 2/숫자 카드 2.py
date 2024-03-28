from collections import defaultdict
N = int(input())
card = list(map(int, input().split()))
M = int(input())
count = list(map(int, input().split()))
num = defaultdict(int)

for i in card:
    num[i] += 1

for i in count:
    print(num[i], end =" ")