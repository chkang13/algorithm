import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input().rstrip())


answer = 0

i = 0
count = 0
while i < m:
    if s[i : i + 3] == "IOI":
        count += 1
        i += 2
        if count == n:
            answer += 1
            count -= 1
    else:
        count = 0
        i += 1
print(answer)