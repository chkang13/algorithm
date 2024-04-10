import sys
input = sys.stdin.readline

N = int(input())
road = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N # 방문 도시 체크

def dfs(start, v, value, count):
    global answer
    visited[v] = 1
    if count == N: # 모든 도시를 다 거쳐간 경우
        if road[v][start] != 0: # 마지막 도시에서 시작도시로 갈 수 있다면
            value += road[v][start] # 마지막 도시에서 시작 도시로의 비용
            if answer > value: # 비용이 더 적게 들었을 경우
                answer = value
        return

    for i in range(N):
        if road[v][i] != 0 and visited[i] == 0 and value < answer: # 두 도시가 연결되어 있고 방문한 적 없으면 + 이미 최소 비용을 넘어간 경우 굳이 갈 필요가 없음(백트래킹)
            dfs(start, i, value + road[v][i], count + 1)
            visited[i] = 0

answer = sys.maxsize # 비용을 최댓값으로 초기화
for v in range(N):
    dfs(v,v,0,1) # 시작 도시, 시작 도시, 비용, 거쳐간 도시 갯수
    visited[v] = 0

print(answer)