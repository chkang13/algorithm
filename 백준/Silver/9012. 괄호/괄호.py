'''
stack 자료구조에 괄호 하나씩을 넣으면서 VPS 가 되면 pop.
')' 괄호가 첫번째에 오는 경우 예외처리 필요.
'''
import sys
input = sys.stdin.readline

t = int(input())
# 괄호 입력
pts = [input().rstrip() for _ in range(t)]

for ps in pts:
    stack = []
    for j in ps:
        if j == '(':
            stack.append(j)
        # ')'인 경우
        else:
            # stack이 비어있을 경우 예외 처리
            if not stack:
                stack.append(j)
                break
            else:
                stack.pop()

    if stack:
        print('NO')
    else:
        print('YES')