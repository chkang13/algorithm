import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))

stack = [] # 스택
receive = [] # 수신한 탑들 번호 저장

for i in range(n):
    if not stack: # 스택이 비어있는 초기 상태
        receive.append(0)

    else:
        while stack:
            if stack[-1][1] > tower[i]: # 현재 값이 작은 경우
                receive.append(stack[-1][0])
                break
            else: # 현재 값이 크거나 같은 경우
                stack.pop()
        
        if not stack: # 스택이 빌 때까지
            receive.append(0)

    stack.append((i+1,tower[i]))
    
print(*receive)