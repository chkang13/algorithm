import sys
input = sys.stdin.readline

x,y = map(int, input().split())
z = (y * 100) // x

if z >= 99: # z가 절대 변하지 않음
    print(-1)
    exit()

left = 0
right = x # 최대 횟수

result = 0
while left <= right:
    mid = (left + right) // 2

    nx = x + mid
    ny = y + mid
    nz = (ny * 100) // nx # 새로운 승률 구하기

    if nz > z: # 범위 변경
        result = mid
        right = mid -1
    else:
        left = mid + 1

print(result)