# 커서를 기준으로 왼쪽 문자열은 left라는 배열에
# 오른쪽 문자열은 right라는 배열에 담는 방식

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    left = []
    right = []

    password = input().rstrip()

    for i in password:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else :
            left.append(i)
    left.extend(reversed(right))
    print("".join(left))