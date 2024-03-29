import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
count = list(map(int, input().split()))

num = {}

for i in card:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

for i in count:
    if i in num:
        print(num[i], end =" ")
    else:
        print(0, end = ' ')