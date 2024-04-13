import sys
input = sys.stdin.readline

n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int,input().split())))


for i in range(1,n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0] # 다음 집을 R로 칠할 때
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1] # 다음 집을 G로 칠할 때
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2] # 다음 집을 B로 칠할 때

print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))