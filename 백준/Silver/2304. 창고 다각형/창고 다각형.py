import sys
input = sys.stdin.readline

n = int(input())

pillars = [] # 기둥 입력 받기
for _ in range(n):
    l, h = map(int, input().split())
    pillars.append((l,h))

pillars.sort() # x 순서대로 정렬

area = 0 # 총 면적

# 가장 긴 기둥의 인덱스 번호
i = 0
for l in pillars :
    if l[1] > area :
        area = l[1] # 최대 기둥 미리 넣기
        max_length = i
    i += 1

pillar = pillars[0] # 처음 시작 기둥
# 맨 왼쪽부터 시작
for i in range(1, max_length+1):
    if pillar[1] < pillars[i][1]: # 더 긴 기둥이면
        area += pillar[1] * (pillars[i][0] - pillars[i-1][0]) # 기둥까지의 면적 구하기
        pillar = pillars[i] # 기둥 시작점 갱신
    else: # 기준점 변경 없이 면적만 더하기
        area += pillar[1] * (pillars[i][0] - pillars[i-1][0]) # 기둥까지의 면적 구하기
    
pillar = pillars[-1] # 마지막 시작 기둥
# 맨 오른쪽부터 시작
for i in range(n-2, max_length-1, -1):
    if pillar[1] < pillars[i][1]:
        area += pillar[1] * (pillars[i+1][0] - pillars[i][0])
        pillar = pillars[i]
    else:
        area += pillar[1] * (pillars[i+1][0] - pillars[i][0])

print(area)