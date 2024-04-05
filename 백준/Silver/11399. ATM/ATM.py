import sys
input = sys.stdin.readline

n = int(input())

times = list(map(int, input().split()))
times.sort() # 정렬

time = 0
for t in range(n):
    time += sum(times[0:t+1])

print(time) 