import sys
input = sys.stdin.readline

n, m =map(int, input().split())

chess = [input().rstrip() for _ in range(n)]
results = []

for i in range(n-7):
    for j in range(m-7):
        w_paint = 0
        b_paint = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'W':
                        w_paint += 1
                    else:
                        b_paint += 1           
                else:
                    if chess[a][b] != 'W':
                        b_paint += 1
                    else:
                        w_paint += 1
        results.append(min(w_paint, b_paint))

print(min(results))                   