'''
1. 모든 숫자 버튼이 고장난 경우 abs(N-100)번 눌러야 한다.
2. 0만 있는 경우부터 9만 있는 경우까지 1000000개의 경우의 수가 나온다!
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))

min_push = abs(N-100) 

for i in range(1000001):
    i = str(i) # 한지릿수씩 찾기 위함
    for j in range(len(i)):
        if int(i[j]) in broken: # 고장난 버튼이 있으면
            break

        elif j == len(i)-1:
            min_push = min(min_push, abs(int(i)-N) + len(i))

print(min_push)