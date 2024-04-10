import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0 # 경우의 수 저장
answer = [] # 부분 수열 저장

def back_track(index, n, s):
    global count

    if sum(answer) == s and len(answer) > 0:
        count += 1

    for i in range(index, n):
        answer.append(nums[i])
        back_track(i+1, n, s)
        answer.pop()

back_track(0,n,s)
print(count)