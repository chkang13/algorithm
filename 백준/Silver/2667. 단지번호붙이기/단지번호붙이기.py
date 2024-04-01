import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
house_num = []
result = 0
count = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y):
    # 범위 및 연결 확인
    if x<0 or x>=n or y<0 or y>=n or graph[x][y] == 0:
        return False
    
    if graph[x][y]:
        global count
        count += 1
        # 방문 처리
        graph[x][y] = 0
        # 네 방향 탐색
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            house_num.append(count)
            result += 1
            count = 0

print(result)
house_num.sort()
print(*house_num, sep='\n')