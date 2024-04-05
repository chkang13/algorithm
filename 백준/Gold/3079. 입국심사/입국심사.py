import sys
input = sys.stdin.readline

n,m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))

left = 0
right = max(time) * m # 시간이 가장 오래 걸리는 경우 초기값
result = 0

while left <= right:
    mid = (left + right) // 2 # 중간값의 시간
    people = 0

    for i in time:
        people += mid // i

    if people < m:
        left = mid + 1
    else : 
        right = mid -1
        result = mid

print(result)