import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
balloon = list(map(int, input().split()))

# 풍선 번호와 적혀있는 수를 같이 저장
q = deque()
for i, num in enumerate(balloon):
    q.append((i+1,num))

# 터트린 순서를 저장
index = []
while q:
     i, num = q.popleft()
     index.append(i)

     # num 만큼 rotate
     if num > 0:
          q.rotate(-num+1)
     else:
          q.rotate(-num)
          
print(*index)