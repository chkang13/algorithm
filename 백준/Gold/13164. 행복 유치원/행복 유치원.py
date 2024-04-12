import sys
input = sys.stdin.readline

n, k = map(int, input().split())

height = list(map(int, input().split()))
between = [] # 키들의 차이값
for i in range(0,n-1):
    between.append(height[i+1]-height[i]) # 원생들 사이의 키차이
    
between.sort() #키차이를 오름차순으로 정렬

sum = 0
for i in range(n-k): #n-k개의 키차이를 더함
    sum += between[i]
    
print(sum)