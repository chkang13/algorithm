import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

pos = list(map(int, input().split()))
pos.sort()

distance = []
for i in range(1, n):
    distance.append(pos[i]-pos[i-1])

distance.sort()
result = sum(distance[:n-k])
print(result)