import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    q = deque()
    doc = list(map(int, input().split()))
    # queue에 삽입
    for i in range(n):
        q.append(doc[i])
    
    # 뽑은 횟수
    count = 0
    while 1:
        # 맨 앞이 우선 순위가 가장 크면
        if q[0] == max(q):
            q.popleft()
            count += 1

            # 궁금한 문서 이면
            if m == 0:
                print(count)
                break

            m -= 1
        
        else:
            q.append(q.popleft())

            # 궁금한 문서이면
            if m == 0:
                m = len(q) - 1 
            else: 
                m -= 1