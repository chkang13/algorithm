import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

# 처음 집의 미세먼지와 공기청정기 위치
house = [list(map(int, input().split())) for _ in range(R)]

# 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def spread(): # 미세먼지 확산 함수
    dust = [[0] * C for _ in range(R)] # 확산된 미세먼지를 저장할 새로운 배열
    
    for x in range(R):
        for y in range(C):
            if house[x][y] > 0: # 미세먼지가 있으면
                
                count = 0
                for d in range(4): # 인접한 네 방향
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 집을 벗어나지 않고 공기청정기가 아니면 확산 진행
                    if 0 <= nx < R and 0 <= ny < C and house[nx][ny] != -1:
                        dust[nx][ny] += house[x][y] // 5 # 확산된 인접 미세먼지
                        count += 1
                
                dust[x][y] += house[x][y] - (house[x][y] // 5) * count # 확산되고 남은 미세먼지
    dust[a1][0] = -1
    dust[a2][0] = -1  
    
    return dust

def rotate(): # 공기청정기 순환 함수
    # 반시계
    for i in range(a1-1, 0, -1):
        house[i][0] = house[i-1][0]
    for i in range(C-1):
        house[0][i] = house[0][i+1]
    for i in range(a1):
        house[i][-1] = house[i+1][-1]
    for i in range(C-1, 0, -1):
        house[a1][i] = house[a1][i-1]

    # 시계
    for i in range(a2+1, R-1):
        house[i][0] = house[i+1][0]
    for i in range(C-1):
        house[-1][i] = house[-1][i+1]
    for i in range(R-1, a2, -1):
        house[i][-1] = house[i-1][-1]
    for i in range(C-1, 0, -1):
        house[a2][i] = house[a2][i-1]

        
    # 공기청정기 옆 위치 0
    house[a1][1] = 0
    house[a2][1] = 0

# 공기청정기 위치 찾기
for i in range(R):
    if house[i][0] == -1:
        a1 = i
        a2 = i+1
        break

for _ in range(T):
    house = spread() 
    rotate()

print(sum(list(sum(i) for i in house)) + 2)