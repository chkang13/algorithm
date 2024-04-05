import sys
input = sys.stdin.readline

n,m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0 # 최솟값
right = max(trees) # 최댓값

# 이진탐색 진행
while left <= right:
    mid = (left + right) // 2 # 중간값
    tree = 0 # 벌목된 나무의 길이

    for h in trees: # 벌목된 나무 길이 계산 
        if h > mid:
            tree += h - mid
    
    if tree >= m: # 이분탐색 범위 재설정
        left = mid + 1
    else:
        right = mid - 1

print(right)