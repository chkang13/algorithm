from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
count = list(map(int, input().split()))
num = defaultdict(int)

for i in card:
    num[i] += 1

for i in count:
    print(num[i], end =" ")