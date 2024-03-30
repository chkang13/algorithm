import sys
input = sys.stdin.readline

n = int(input())

room = [input().rstrip() for _ in range(n)]

ver_count = 0
hir_count = 0
for i in range(n):
    ver = 0
    hir = 0
    for j in range(n):
        if room[i][j] == '.':
            ver += 1
        else:
            ver = 0
        if ver == 2:
            ver_count += 1

        if room[j][i] == '.':
            hir += 1
        else:
            hir = 0
        if hir == 2:
            hir_count += 1

print(ver_count, hir_count)