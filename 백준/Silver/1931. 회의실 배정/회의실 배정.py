'''
빨리 끝나는 회의 순서로 정렬, 같을 경우 빨리 시작하는 순서로 정렬
'''
import sys
input = sys.stdin.readline

n = int(input())

time = []
for i in range(n):
    s,e = map(int, input().split())
    time.append((s,e))

# 람다를 이용한 정렬
time.sort(key = lambda x : (x[1], x[0]))

count = 1 # 회의 수 세기 
end_time = time[0][1] # 첫 회의 끝나는 시간

for i in range(1, n):
    if time[i][0] >= end_time: # 다음 회의의 시작시간이 더 뒤면
        end_time = time[i][1]
        count += 1

print(count)