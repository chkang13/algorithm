import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
m = int(input())
cands = [input().rstrip() for _ in range(m)]

s = ''
e = ''

if n == 1:
    print(cands[0])
    exit(0)
    
for i in range(len(words)):
    if words[i] == '?':
        if i == 0:
            e = words[i+1][0]
        elif i == n-1:
            s = words[i-1][-1]
        else:
            s = words[i-1][-1]
            e = words[i+1][0]

for i in range(len(cands)):
    if cands[i] in words:
        continue
    if s == '':
        if cands[i][-1] == e:
            print(cands[i])
    elif e == '':
        if cands[i][0] == s:
            print(cands[i])
    
    if cands[i][0] == s and cands[i][-1] == e:
        print(cands[i])
