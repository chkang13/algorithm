import sys
input = sys.stdin.readline

n = int(input())

ent = {input().rstrip():i for i in range(n)}
ext = {input().rstrip():i for i in range(n)}

over = 0
out = list(ext.keys())
for i in range(n-1):
    for j in range(i+1, n):
        if ent[out[j]] < ent[out[i]]:
            over += 1
            break

print(over)