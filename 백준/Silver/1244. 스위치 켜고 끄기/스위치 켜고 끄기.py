import sys
input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))
student = int(input())

changes = []
for _ in range(student):
    m, num = map(int,input().split())
    changes.append((m,num))

for change in changes:
    # 남자
    if change[0] == 1:
        for i in range(1, n+1):
            if i % change[1] == 0:
                if switch[i] == 0:
                    switch[i] = 1
                else: switch[i] = 0
    # 여자
    else:
        # 양 옆 바꾸기
        for j in range(1, n // 2):
            if change[1]-j < 1 or change[1]+j > n: break
            if switch[change[1] - j] == switch[change[1] + j]:
                if switch[change[1] - j] == 0:
                    switch[change[1] - j] = 1
                else: switch[change[1] - j] = 0
                if switch[change[1] + j] == 0:
                    switch[change[1] + j] = 1
                else: switch[change[1] + j] = 0
            else: break
        # 자기 자신 바꾸기    
        if switch[change[1]] == 0:
            switch[change[1]] = 1
        else: switch[change[1]] = 0

for i in range(1, n+1):
    print(switch[i], end = ' ')
    if i % 20 == 0:
        print()