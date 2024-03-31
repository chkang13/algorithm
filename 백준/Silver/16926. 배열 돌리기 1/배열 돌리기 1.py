# 제한조건에 따라 사각형을 돌지 않는 경우가 없음
# 시간 초과
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    # 돌아가는 사각형 갯수
    for i in range(min(n,m)//2):
        start = arr[i][i]
        # 하로 이동
        for j in range(i+1, n-i):
            temp = arr[j][i]
            arr[j][i] = start
            start = temp
        # 우로 이동
        for j in range(i+1,m-i):
            temp = arr[n-i-1][j]
            arr[n-i-1][j] = start
            start = temp
        # 상으로 이동
        for j in range(i+1, n-i):
            temp = arr[n-j-1][m-i-1]
            arr[n-j-1][m-i-1] = start
            start = temp
        # 좌로 이동
        for j in range(i+1, m-i):
            temp = arr[i][m-j-1]
            arr[i][m-j-1] = start
            start = temp

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()