import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0] 
total = road[0] * price[0] # 처음 도시에서 다음 도시까지 이동

for i in range(1, n-1):
    if price[i] < min_price:
        min_price = price[i]
    
    total += min_price * road[i]

print(total)