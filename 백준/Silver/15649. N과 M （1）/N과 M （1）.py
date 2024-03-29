import sys
input = sys.stdin.readline

N,M = map(int, input().split())

visited = [False] * N
answer = []

def back_track(index, N, M):
    if index == M:
        print(*answer)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] =True
            answer.append(i+1)
            back_track(index+1, N, M)
            visited[i] = False
            answer.pop()

back_track(0,N,M)