import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    fashion = defaultdict(list)
    count = 1

    for _ in range(n): # 의상과 종류를 딕셔너리에 저장
        cloth, part = input().rstrip().split()
        fashion[part].append(cloth)
    
    for i in fashion:
        count *= (len(fashion[i]) + 1)
    print(count - 1) # 아무것도 입지 않는 경우를 빼줘야함
